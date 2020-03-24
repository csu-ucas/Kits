#include <iostream>
#include <communicator/sender.h>
#include <communicator/receiver.h>

using namespace std;

int main() {
    Receiver * rcv = new Receiver(23333);
    
    Sender * sdn = new Sender("localhost", 23333);
}
