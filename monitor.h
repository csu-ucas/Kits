#ifndef MONITOR_H
#define MONITOR_H

enum State {
    ACTIVE,
    DEAD,
    READY,
    OCCUPIED
};

class Monitor {
private:
    int monitor_id;
    /* Private functions that are limited-used by
     * class-internal process. */
    State get_sensor_status();
    float get_cpu_workload();
    State get_FPGA_status();

public:
    Monitor();
    ~Monitor();
    bool run(); 
};

#endif