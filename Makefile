CFLAGS = -O
CC = g++

receive_test: receiver.o recv_test.o
	$(CC) $(CFLAGS) recv_test.o receiver.o -o receive_test

sender_test: sender.o send_test.o
	$(CC) $(CFLAGS) send_test.o sender.o -o sender_test

sender.o:
	$(CC) $(CFLAGS) -c sender.cpp

receiver.o:
	$(CC) $(CFLAGS) -c receiver.cpp

comm_test.o: comm_test.cpp 
	$(CC) $(CFLAGS) -c comm_test.cpp



clean:
	rm -f core *.o 