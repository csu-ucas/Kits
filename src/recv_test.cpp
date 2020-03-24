#include <communicator/receiver.h>
#include <iostream>
using namespace std;
int main() {
    int port = 23333;
    Receiver * rcv = new Receiver(port);
    for (int i = 0; i < 5; i++) {
        rcv->receive();
    } 
    for (int i = 0; i < 5; i++) {
        cout << rcv->msgq->front() << endl;
        rcv->msgq->pop();
    }
    rcv->~Receiver();

}