#ifndef MONITOR_H
#define MONITOR_H

#include <string>
#include "sensor.h"
#include "communicator.h"
enum State {
    ACTIVE,
    DEAD,
    READY,
    OCCUPIED
};

class Monitor {
private:
    int monitor_id;
    Communicator * cmt;
    
    /* Private functions that are limited-used by
    * class-internal process. */
    State get_sensor_status();

    float get_cpu_workload();
    
    State get_FPGA_status();

    // Fetching directly from docker
    State fetch_schedule_result();

    // Fetching such info from c-agent
    std::string fetch_schedule_info();

    // Writting to etcd

    // Sending a copy of info that are originally
    // to etcd to c-agent


public:
    Monitor();

    ~Monitor();

    bool run(); 
};

#endif