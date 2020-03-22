#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <sys/types.h>
    
void error(const char * msg) {
    perror(msg);
}

#endif