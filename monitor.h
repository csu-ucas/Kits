#ifndef MONITOR_H
#define MONITOR_H

#include <string>
#include "sender.h"
#include "receiver.h"

enum State {
    ACTIVE,
    DEAD,
    READY,
    OCCUPIED
};

class Monitor {
private:
    int monitor_id;
    Sender * send_etcd;
    Receiver * recv_etcd;
    
    Sender * send_cagent;
    Receiver * recv_schd;
    
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
    bool send_pulse_etcd();
    
    // Sending a copy of info that are originally
    // to etcd to c-agent
    bool send_pulse_cagent();

    

public:
    Monitor();

    ~Monitor();

    bool run(); 
};

#endif
