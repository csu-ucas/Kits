#include "communicator.h"


int main() {
    int port = 23333;
    Communicator * cmt = new Communicator("localhost", port);
    const char * buffer = "Hello, world";
    cmt->send("We are the world");
    return 0;
}
// #include"test.h"

// 　　int main()

// 　　{

// 　　 fun(); 

// 　　}