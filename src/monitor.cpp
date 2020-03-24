#include <monitor/monitor.h>
#include <monitor/peaker.h>
#include <communicator/receiver.h>
#include <communicator/sender.h>
#include <dockertask.h>
#include <utils>
#include <iostream>
#include <pthread.h>




Monitor::Monitor(int id) {
    this->monitor_id = id;

}
