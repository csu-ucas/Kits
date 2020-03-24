#include <iostream>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h> 
#include <communicator/sender.h>
#include <utils.h>


Sender::Sender(std::string serv_hostname_str, int serv_port) {
    const char * serv_hostname = serv_hostname_str.c_str();
    this->if_established = false;
    struct hostent * server = gethostbyname(serv_hostname);
    this->serv_port = serv_port;
    this->sockfd = socket(AF_INET, SOCK_STREAM, 0);
    
    /* Checking validity of socket defined */
    if (this->sockfd < 0) {
        error("ERROR opening socket\n");
    }

    if (server == NULL) {
        error("ERROR, no such host\n");
        
    }
    /* Copying value from server to serv_addr */
    bzero((char *)&this->serv_addr, sizeof(this->serv_addr));
    this->serv_addr.sin_family = AF_INET;
    bcopy((char *)(server)->h_addr, 
         (char *)&(this->serv_addr).sin_addr.s_addr,
         server->h_length);
    this->serv_addr.sin_port = htons(this->serv_port);
    
    /* Checking connectivity of socket */
    if (connect(this->sockfd,(struct sockaddr *) & 
        this->serv_addr,sizeof(this->serv_addr)) < 0) {
        error("ERROR connecting");
    } else {
        this->if_established = true;
    }                  
}

bool Sender::send(std::string msg) {
    const char * msg_c = msg.c_str();
    int n = 0;
    printf("%s, %d", msg_c, (int)strlen(msg_c));
    n = write(sockfd,msg_c, strlen(msg_c));
    close(sockfd);
    return 0;                
}
