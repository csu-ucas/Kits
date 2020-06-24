import time
import socket 
import errno
import os 
from random import randint

class MasterVoter(object):
    def __init__(self):
        self.__provision()

    def __provision(self):
        self.listening_socket = self.__getSock()
        pass 
        

    def __getSock(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for i in range(10, 65536):
            
            try:
                print("Checking port %d"%(i))
                s.bind(("localhost", i))
                return s 
            except socket.error as e:
                print(e)
                print("Port %d already in use, Checking %d"%(i, i+1))
                continue 
        return s 
    
    def __send(self, hostname, str):
        pass 

    def __getSelfIp(self):
        pass
    
if __name__ == "__main__":
    mv = MasterVoter()
    print(mv.listening_socket.getsockname())



            

        