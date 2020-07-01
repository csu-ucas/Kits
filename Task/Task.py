from  MasterVoter.Node import Node
from Task.Comp import Comp
import datetime
import mysql.connector

class Task:
    # init
    def __init__(self,name, containerCopies, imageList, specifyNode,
                 compType, compNum, compMemory, compStorage):
        sql="select * from `tasks` where name='"+name+"'"
        if len(self.__connectDb(sql))>=1:
            print('ERROR: This name already exited')
            return

        self.name=name
        self.__containerCopies = containerCopies
        self.__imageList = imageList
        if(specifyNode == None):
            self.__specifyNode = self.__initNode() 
        else:
            self.__specifyNode = specifyNode
        self.__comp = Comp(compType)
        self.__compNum = compNum
        self.__compMemory = compMemory
        self.__compStorage = compStorage
        self.createTime = datetime.datetime.strftime(
            datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

        sql="insert into `tasks`(`name`,`containerCopies`,`imageList`, \
            `specifyNode`,`compType`,`compNum`,`compMemory`,`compStorage`, \
            `createTime`) values('"+name+"',"+containerCopies+",'"+imageList+ \
            "','"+ specifyNode+"','"+compType+"',"+compNum+",'"+compMemory+ \
            "','"+ compStorage+"','"+self.createTime+"'"
        self.__connectDb(sql)
        
    def __connectDb(self,sql):
        mydb = mysql.connector.connect(
            host="localhost",      
            user="root",    
            database="TasksInfo"   
        )
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        return mycursor
    
    def query(self,sql):
        return self.__connectDb(sql)
    
    # choose a suitable Node
    def __initNode(self):
        return 
if __name__ == "__name__":
    Task.query("select * from `tasks`")