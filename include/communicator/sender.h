#ifndef SENDER_H
#define SENDER_H 

#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

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
};

#endif