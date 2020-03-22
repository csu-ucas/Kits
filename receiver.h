#ifndef RECEIVER_H
#define RECEIVER_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

class Receiver {
private:
    int listen_sockfd;
    int accept_sockfd;
    int port;
    socklen_t client_len;
    char buffer[256];
    struct sockaddr_in serv_addr;
    struct sockaddr_in cli_addr;

public:
    Receiver(int port);
    ~Receiver();
    char * receive();
};




#endif