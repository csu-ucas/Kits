#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>

void error(const char * msg) {
    perror(msg);

}

#endif