#ifndef RECEIVER_H
#define RECEIVER_H

#include <string>
#include <queue>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
using namespace std; 

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
    queue<std::string> * msgq;
    Receiver(int port);
    ~Receiver();
    void receive();
    int get_client_port();
    std::string get_client_ip();
    void run();
};




#endif