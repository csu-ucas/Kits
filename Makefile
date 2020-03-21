CFLAGS = -O
CC = g++

test: communicator.o comm_test.o
	$(CC) $(CFLAGS) comm_test.o communicator.o -o test

communicator.o:
	$(CC) $(CFLAGS) -c communicator.cpp

comm_test.o: comm_test.cpp 
	$(CC) $(CFLAGS) -c comm_test.cpp



clean:
	rm -f core *.o 