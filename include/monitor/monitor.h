#ifndef MONITOR_H
#define MONITOR_H

#include <string>
#include <communicator/sender.h>
#include <communicator/receiver.h>
#include <utils.h>

class Monitor {
private:
    int monitor_id;

public:
    Monitor();

    ~Monitor();

    bool run(); 
};

#endif
