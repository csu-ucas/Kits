#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <sys/types.h>
#include <string.h>

void error(const char * msg) {
    perror(msg);
}

std::string fetch_terminal(std::string cmd) {
    char buffer[0x100];
    bzero(buffer, sizeof(buffer));
    FILE * fs = NULL;
    fs = popen(cmd.c_str(), "r");
    fget(buffer, sizeof(buffer), fs);
    pclose(fs);
    std::string ret(buffer);
    return ret;
}

#endif