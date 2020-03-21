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

#endif