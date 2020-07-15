import datetime
import mysql.connector
import docker
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
fatherPath = os.path.abspath( \
                            os.path.dirname(current_path) \
                            + os.path.sep + ".")
sys.path.append(fatherPath)  

from Executor.Executor import Executor

class Task:
    '''
    init
    'specifyNode' signify which node to run the task
    (if user dosen't choose the special node ,
     __initNode will choose a proper node).
    'compType' signify that the task use CPU or GPU or FPGA.
    'compNum' signify the number of comp
    'compMemory' limit the memory to run the task
    'compStorage' limit the storage to run the task
    '''

    def __init__(self, name, specifyNode,containerPaths,
                 compType, compNum, compMemory,priority):
        sql = "select * from `tasks` where name='" + name + "'"
        if len(self.__connectDb(sql)) >= 1:
            print('ERROR: This name already exites')
            return

        self.__containers=[]
        self.__name = name
        if(specifyNode == None):
            self.__specifyNode = self.__initNode()
        else:
            self.__specifyNode = specifyNode
        self.__containerPaths=containerPaths
        self.__comp = compType
        self.__compNum = compNum
        self.__compMemory = compMemory
        self.__createTime = datetime.datetime.strftime(
            datetime.datetime.now(), '%Y-%m-%d %H:%M:%S.%f')
        self.__priority=priority

        
    def getContainerNames(self):
        names=''
        for i,container in enumerate(self.__containers):
            names+=(container.name)
            if i + 1 != len(self.__containers):
                names += ','
        return names

    def deleteSelf(self):
        sql="delete from tasks where name='" +\
            self.__name+"'"
        self.__connectDb(sql)

    # change user and password for special database
    def __connectDb(self, sql):
        mydb = mysql.connector.connect(
            host="localhost",
            user='debian-sys-maint',
            password='iJol6nb2K1IHxQa8',
            database="TasksInfo"
        )
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        if not (sql[0:5] == str('selec')):
            mydb.commit()
            return mycursor
        else:
            return mycursor.fetchall()

    def getContainers(self):
        executor = Executor()
        for path in self.__containerPaths:
            self.__containers.append(executor.executeFile(path))

        sql = "insert into `tasks`(`name`,`containers`,"+ \
            " `specifyNode`,`compType`,`compNum`,"+ \
            "`compMemory`,`createTime`,`priority`) values('" + \
            self.__name + "','" + self.getContainerNames()+"','"  + \
            str(self.__specifyNode) + "','" + self.__comp + "'," +\
            str(self.__compNum) +",'" + self.__compMemory + "','" +\
            self.__createTime + "','"+str(self.__priority) + "')"
        print(sql)
        # self.__connectDb(sql)



    def forSortTime(self):
        return self.__createTime
    
    def forSortPriority(self):
        return self.__priority,self.__createTime

    # choose a suitable Node
    def __initNode(self):
        return
