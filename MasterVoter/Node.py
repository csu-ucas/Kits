import os
import socket
import mysql.connector
from getmac import get_mac_address as gma

GATEWAY = "10.255.255.255"


class Node(object):
    def __init__(self, role):
        self.__mac = gma()
        self.__ip = self.__getIP()
        self.__role = role
        self.__db = mysql.connector.connect(
                host="localhost",
                user="root",
                database="NodesInfo"
        )
        self.__dbcursor = self.__db.cursor(buffered=True)
        if len(self.__checkRegistered(self.__mac)) == 1:
            self.__updateField([('UpdateTime', 'current_timestamp'),],\
                    ("NodeMac",self.__mac))
        else:
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
                values ('%s','%s','%s')"%(self.__ip,\
                self.__mac, self.__role)
        self.__dbcursor.execute(regis_sql)
        self.__db.commit()
    
    def __checkRegistered(self, mac):
        checksql = "select * from nodes\
                where NodeMac='%s';"%(mac)
        result = self.__checkInfo(checksql).fetchall()
        return result
    '''
    Note that `restriction` is a tuple of a key and a value
    where field of 'string' should be pre-quoted;
    'fields' is a list of tuples that contains two-element field
    including its key and its target value.
    '''
    def __updateField(self, fields, restriction):
        field_str = ""
        for field in fields:
            field_key = field[0]
            field_val = '%s'%(field[1]) if\
                    type(field[1])==str else field[1]
            field_str += "%s=%s,"%(field_key, field_val)
        field_str = field_str[:-1]+' '
        update_sql = "update nodes set %s where %s='%s'"\
                %(field_str, restriction[0], restriction[1])
        print(update_sql)
        self.__dbcursor.execute(update_sql)
        self.__db.commit() 


    def __checkInfo(self, string):
        self.__dbcursor.execute(string)
        dbResponse = self.__dbcursor
        self.__db.commit()
        return dbResponse
        
    def changeRole(self, targetRole):
        self.__updateField([('NodeRole', targetRole),],\
                ('NodeMac', self.__mac))

    def changeIP(self, targetIP):
        self.__updateField([('NodeHostname', targetIP),],\
                ('NodeMac', self.__mac))
    
    def changeConnection(self, connStatus):
        self.__updateField([('NodeConnected', int(connStatus)),],\
                ('NodeMac', self.__mac))


if __name__ == "__main__":
    node = Node("Master")

    #node.changeRole('Master')

    
