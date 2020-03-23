#ifndef UTILS_H
#define UTILS_H

typedef struct {
    std::string target_name;
    std::string domain_name;
    int target_port;
}Target;

enum State {
    ACTIVE,
    DEAD,
    READY,
    OCCUPIED
};


void error(const char * msg);

std::string fetch_terminal(std::string cmd);

bool port_regis(std::string name, std::string hostname, int port);

#endif