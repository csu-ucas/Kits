#include "receiver.h"
// #include "sender.h"

int main() {
    int port = 23333;
    Receiver * rcv = new Receiver(port);
    // Sender * cmt = new Sender("localhost", port);
    // const char * buffer = "Hello, world";
    // cmt->send("We are the world");
    // return 0;
}