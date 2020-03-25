#include <monitor/monitor.h>
#include <monitor/peaker.h>
#include <dockertask.h>
#include <utils.h>
#include <iostream>
#include <cstdlib>
#include <pthread.h>



Monitor::Monitor(int id) {
    this->id = id;
    this->peaker = new Peaker();
}

void Monitor::assign_task(DockerTask * task) {
    this->peaker->add_task(task);
}

std::string Monitor::get_pulse() {
    return this->peaker->make_pulse();
}