// #include "receiver.h"
#include "sender.h"
#include <iostream>


int main() {
    int port = 23333;
    // Receiver * rcv = new Receiver(port);
    Sender * cmt = new Sender("localhost", port);
    std::string msg = "Hello, world";
    cmt->send(msg);
    return 0;
}