#include "monitor.h"

Monitor::Monitor() {
    this->cmt = Communicator()
}

State Monitor::get_sensor_status();

float Monitor::get_cpu_workload();

State Monitor::get_FPGA_status();

State Monitor::fetch_schedule_result();

std::string Monitor::fetch_schedule_info();