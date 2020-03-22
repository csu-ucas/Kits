#ifndef SENDER_H
#define SENDER_H 

#define SERV_MOD 0x0
#define CLNT_MOD 0x1
#define BUFF_SIZE 0xf000

#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include "sender.h"

class Sender {
private:
    bool if_established;
    int sockfd;
    int serv_port;
    struct sockaddr_in serv_addr;

public:
    Sender(std::string serv_hostname_str, int serv_port);
    ~Sender(); 
    bool send(std::string msg);
    bool recv(char msg);
};

#endif