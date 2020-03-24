#include <vector>
#include <iostream>

class Peaker {
private:
    int monitor_id;
    vector<Task *> tasks;
    /* Private functions that are limited-used by
    * class-internal process. */
    State get_sensor_status();

    float get_cpu_workload();
    
    State get_FPGA_status();

    State get_docker_status();

    

public:
    Monitor();

    ~Monitor();

    bool add_task(Task * task);

    std::string make_pulse();

    bool run(); 
};