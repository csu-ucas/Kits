from Task.Comp import Comp
import datetime
import mysql.connector

class Task:
    '''
    init
    'containerCopies' is the number of containers.
    'imageList' is the images user need.
    'specifyNode' signify which node to run the task
    (if user dosen't choose the special node ,
     __initNode will choose a proper node).
    'compType' signify that the task use CPU or GPU or FPGA.
    'compNum' signify the number of comp
    'compMemory' limit the memory to run the task
    'compStorage' limit the storage to run the task
    '''
    def __init__(self,name, containerCopies, imageList, specifyNode,
                 compType, compNum, compMemory, compStorage):
        sql="select * from `tasks` where name='"+name+"'"
        if len(self.__connectDb(sql))>=1:
            print('ERROR: This name already exites')
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
    
    # choose a suitable Node
    def __initNode(self):
        return 
