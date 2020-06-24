import os
import socket
import mysql.connector
from getmac import get_mac_address as gma

GATEWAY = "10.255.255.255"


class Node(object):
    def __init__(self, role):
        self.mac = gma()
        self.ip = self.__getIP()
        self.role = role
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            database="NodesInfo"
        )
        self.dbcursor = self.db.cursor()
        self.__registerNode()
    
    def __getIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((GATEWAY, 1))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def __registerNode(self):
        regis_sql = "insert into nodes\
            (NodeHostname, NodeMac, NodeRole)\
            values ('%s','%s','%s')"%(self.ip, self.mac, self.role)
        self.dbcursor.execute(regis_sql)
        self.db.commit()

    def checkInfo(self, string):
        dbResponse = self.dbcursor.execute(string)
        return dbResponse
        

if __name__ == "__main__":
    node = Node("Master")
    
    
