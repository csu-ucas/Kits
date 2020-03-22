#ifndef SENDER_H
#define SENDER_H 

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

class Sender {
private:
    bool if_established;
    int sockfd;
    int serv_port;
    struct sockaddr_in serv_addr;

public:
    Sender(char * serv_hostname, int serv_port);
    ~Sender(); 
    bool send(const char * buffer);
    bool recv(char msg);
};

#endif