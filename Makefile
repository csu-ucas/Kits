CFLAGS = -O
CC = g++

synth: utils.o receiver.o sender.o sync-test.o
	$(CC) $(CFLAGS) utils.o receiver.o sender.o sync-test.o -o synth 

receive_test: receiver.o recv_test.o utils.o
	$(CC) $(CFLAGS) recv_test.o receiver.o utils.o -o receive_test

sender_test: sender.o send_test.o utils.o
	$(CC) $(CFLAGS) send_test.o sender.o utils.o -o sender_test

utils.o:
	$(CC) $(CFLAGS) -c utils.cpp 

sender.o: utils.o 
	$(CC) $(CFLAGS) -c sender.cpp

receiver.o: utils.o
	$(CC) $(CFLAGS) -c receiver.cpp

clean:
	rm -f core *.o 