# Kubenetes in the Sky (Kits)
## Prerequisite
0. cmake
1. Linux Kernel 
2. GNU C++ compiler >=4.8 (which should support C++11)

## Developing and Debugging Process
0. Please checkout to a new branch before you make any modifications
1. Put your header files in `$BASE_DIR/include` and source files (.cpp) at `$BASE_DIR/src`
2. Modify `CMakeLists.txt` over the source files you would like to include
3. run `cmake .`
4. run `make`
5. run `./debug`
6. Remove all your binaries and cmake caches before you commit

## Modules
### Monitor (by xwan)
2 interfaces provided:
1. Add task: `void Monitor::assign_task(DockerTask * task)` where `DockerTask` is defined in `./include/dockertask.h`
2. get_pulse: `std::string Monitor::get_pulse()` returning a string indicating status of computing units, sensors and docker tasks
### Communicator (by xwan)
1. Message Sender
```c++
#include <communicator/sender.h>        // Include the header

int main() {
    int port = 23333;
    // Sender(std::string hostname, int port)
    Sender * cmt = new Sender("localhost", port);
    std::string msg = "Hello, world";   // Message to be sent
    cmt->send(msg);
    delete cmt;                         // Very important
    return 0;
}
```
2. Message Receiver
```c++
#include <communicator/receiver.h>      // Include the header
#include <iostream>
using namespace std;
int main() {
    int port = 23333;
    Receiver * rcv = new Receiver(port);
    for (int i = 0; i < 5; i++) {       //Receiving msg for 5 times
        rcv->receive();
    } 
    for (int i = 0; i < 5; i++) {
        cout << rcv->msgq->front() << endl; // Fetching 1 message from receiver
        rcv->msgq->pop();                   // Pop the queue
    }
    rcv->~Receiver();
    delete rcv;
}
```
