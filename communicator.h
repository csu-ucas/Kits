#ifndef COMMUNICATOR_H
#define COMMUNICATOR_H



#define SERV_MOD 0x0
#define CLNT_MOD 0x1
#define BUFF_SIZE 0xf000

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

void error(const char * msg) {
    perror(msg);
}


class Communicator {
private:
    bool if_established;
    int sockfd;
    int serv_port;
    struct sockaddr_in serv_addr;


public:
    Communicator(char * serv_hostname, int serv_port);
    ~Communicator(); 
    bool send(const char * buffer);
    bool recv(char msg);
};


Communicator::Communicator(char * serv_hostname, int serv_port) {
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

bool Communicator::send(const char * buffer) {
    int n = 0;
    printf("%s, %d", buffer, strlen(buffer));
    n = write(sockfd,buffer,strlen(buffer));
    close(sockfd);
    return 0;                
}

#endif