#ifndef MONITOR_H
#define MONITOR_H

#include <string>
#include "sender.h"
#include "receiver.h"
#include "utils.h"

class Monitor {
private:
    int monitor_id;

public:
    Monitor();

    ~Monitor();

    bool run(); 
};

#endif
