#ifndef MONITOR_H
#define MONITOR_H

#include <monitor/monitor.h>
#include <monitor/peaker.h>
#include <dockertask.h>
#include <utils>
#include <iostream>
#include <pthread.h>

class Monitor {
private:
    int monitor_id;
    Peaker * pkr;
    
public:
    Monitor();

    ~Monitor();

    assign_task(DockerTask * task);

    std::string get_pulse() {
};

#endif
