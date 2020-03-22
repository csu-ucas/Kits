#include "monitor.h"
#include "utils.h"
#include <iostream>
#include <string.h>
Monitor::Monitor(int id) {
    this->monitor_id = id;
}


State Monitor::get_sensor_status();

float Monitor::get_cpu_workload() {
    std::string cmd = "mpstat | grep all | awk -F \" \" '{print $NF}'";
    std::strstream ss;
    ss << cmd;
    float ret = 0;
    ss >> ret;
    return ret;
}

// State Monitor::get_FPGA_status();

State Monitor::fetch_schedule_result();

std::string Monitor::fetch_schedule_info();