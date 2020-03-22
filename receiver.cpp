
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include "receiver.h"
#include "utils.h"

Receiver::Receiver(int port) {
    this->msgq = new queue<std::string>();
    this->listen_sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (this->listen_sockfd < 0) 
        error("ERROR opening socket");
    bzero((char *) &this->serv_addr, sizeof(this->serv_addr));
    this->port = port;
    this->serv_addr.sin_family = AF_INET;
    this->serv_addr.sin_addr.s_addr = INADDR_ANY;
    this->serv_addr.sin_port = htons(this->port);
    /* binding */
    if (bind(this->listen_sockfd, (struct sockaddr *)&this->serv_addr,
            sizeof(this->serv_addr)) < 0) 
            error("ERROR on binding");
    /* listening */

}

Receiver::~Receiver() {
    close(this->accept_sockfd);
    close(this->listen_sockfd);
}
void Receiver::receive() {
    listen(this->listen_sockfd,5);
    
    this->client_len = sizeof(this->cli_addr);
    /* accepting */
    this->accept_sockfd = accept(this->listen_sockfd, 
                (struct sockaddr *) &this->cli_addr, 
                &this->client_len);
    
    if (this->accept_sockfd < 0) 
        error("ERROR on accept");
    bzero(this->buffer,256);
    int n = read(this->accept_sockfd,this->buffer,255);
    if (n < 0) 
        error("ERROR reading from socket");
    printf("Here is the message: %s\n", this->buffer);
    std::string msg(this->buffer);
    this->msgq->push(msg);

    n = write(this->accept_sockfd,"I got your message", 18);
    if (n < 0) 
        error("ERROR writing to socket");
}