import os
import socket
import mysql.connector
import threading 
import json 
from getmac import get_mac_address as gma
from utils import ping
from queue import Queue

GATEWAY = "10.255.255.df255"
LISTEN_PORT = 23333
INIT_CONTACT_IP = '10.2.25.68'


class Node(object):
    def __init__(self, role):
        self.__mac = gma()
        self.__ip = self.__getIP()
        self.__role = role
        self.__members = {self.__mac:self.__ip}
        self.__msgq = Queue()
        self.__msgqSemaph = threading.Semaphore(0)

        # Start receiving messages here, multithreads are used
        self.__lisnSock = self.__getSock()
        self.__db = mysql.connector.connect(
                host="localhost",
                user="root",
                database="NodesInfo"
        )
        self.__dbcursor = self.__db.cursor(buffered=True)
        self.__registerNode(self.__ip, self.__mac, self.__role)
        self.__procFuncDict = {
            'query': self.__query,
            'join': self.__join,     # only valid when role is Master
            'vote': self.__vote,
            'order': self.__order,
        }

    
    def __getSock(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for i in range(23333, 65536):
            try:
                print("Checking port %d"%(i))
                s.bind(("localhost", i))
                # LISTEN_PORT = i
                return s 
            except socket.error as e:
                print(e)
                print("Port %d already in use, Checking %d"%(i, i+1))
                continue 
        return -1   
        
    def __getIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((GATEWAY, 1))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def __registerNode(self, ip, mac, role):
        if len(self.__checkRegistered(self.__mac)) == 1:
            self.__updateField([('UpdateTime', 'current_timestamp'),],\
                    ("NodeMac",self.__mac))
        else:
            regis_sql = "insert into nodes\
                    (NodeHostname, NodeMac, NodeRole)\
                    values ('%s','%s','%s')"%(ip, mac, role)
            self.__dbcursor.execute(regis_sql)
            self.__db.commit()
    
    def __checkRegistered(self, mac):
        checksql = "select * from nodes\
                where NodeMac='%s';"%(mac)
        result = self.__checkInfo(checksql).fetchall()
        return result
    
    def __updateField(self, fields, restriction):
        '''
        Note that `restriction` is a tuple of a key and a value
        where field of 'string' should be pre-quoted;
        'fields' is a list of tuples that contains two-element field
        including its key and its target value.
        '''
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
        
    def __changeRole(self, targetRole):
        self.__updateField([('NodeRole', targetRole),],\
                ('NodeMac', self.__mac))

    def __updateIP(self, targetIP):
        self.__updateField([('NodeHostname', targetIP),],\
                ('NodeMac', self.__mac))
    
    def __changeConnection(self, connStatus):
        self.__updateField([('NodeConnected', int(connStatus)),],\
                ('NodeMac', self.__mac))

    def __send(self, targetIP, targetPort, message):
        send_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_skt.connect((targetIP, targetPort))
        send_skt.sendall(message.encode())
        send_skt.close()

    def __query(self, msg_body):
        checksql = "select NodeMac, NodeHostname"\
            + "from nodes where NodeRole='Master'"
        master_mac, master_ip = self.__checkInfo(checksql)
        ret_msg = json.dumps({
            'master_mac': master_mac,
            'master_ip': master_ip,
            # 'msg_hash': msg_body['msg_hash']
        })
        self.__send(msg_body['ip'], msg_body['port'], ret_msg)
        

    def __vote(self, msg_body):
        pass 

    def __join(self, msg_body):
        # if self.__role == 'Slave':
        #     msg = 
        # elif self.__role == 'Master':
        self.__registerNode(msg_body['ip'], msg_body['mac'], 'Slave')
        for member_mac in self.__members.keys():
            msg = json.dumps({
                'type':'order',
                'message': {
                    'command':'join node',
                    'ip':msg_body['ip'],
                    'mac':msg_body['mac']
                }
            })
            self.__send(member_mac, self.__members[member_mac], msg)
    
    def __order(self, msg_body):
        if self.__checkRegistered(msg_body['mac']):
            pass 
        else:
            self.__registerNode(msg_body['ip'], msg_body['mac'], 'Slave')
        
    def __msgReceive(self, sock):
        while True:
            conn = sock.accept()
            message = conn[0].receive(0x400).decode()
            if not message:
                continue 
            else:
                self.__msgq.put(message)
                self.__msgqSemaph.release()
        raise Exception("Socket for receiving exited unexpectedly.")
    
    def __msgDealer(self):
        while True:
            self.__msgqSemaph.acquire()
            msg = self.__msgq.get()
            info = json.loads(msg)
            '''
            info = {
                type:"" (query, join_cluster, vote_info, order),
                'body':{
                    port:int
                    ip: str
                    syncInfoHash: str
                }
            }
            '''
            self.__procFuncDict[info['type']](info['body'])

    def run(self):
        thread_msgDealer = threading.Thread(target=self.__msgDealer, args=())
        thread_msgDealer.start()
        thread_msgListen = threading.Thread(target=self.__msgReceive, target=(self.__lisnSock,))
        thread_msgListen.start()
        if self.__role == 'Slave':
            query_rq = (json.dumps({
                'type':'query',
                'message':{
                    'ip':self.__ip，
                    'port': LISTEN_PORT
                }
            }))
            send_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            send_skt.connect((INIT_CONTACT_IP, targetPort))
            send_skt.sendall(message.encode())
            send_skt.close()
            




if __name__ == "__main__":
    node = Node("Master")

    #node.changeRole('Master')

    
