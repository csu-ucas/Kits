#include <vector>
#include "peaker.h"
float Peaker::get_cpu_workload() {
    std::string cmd = "mpstat | grep all | awk -F \" \" '{print $NF}'";
    std::string msg = fetch_terminal(cmd);
    std::strstream ss;
    ss << msg;
    float ret = 0;
    ss >> ret;
    return ret;
}