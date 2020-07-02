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

    def __init__(self, name, containerCopies, image, specifyNode,
                 compType, compNum, compMemory):
        sql = "select * from `tasks` where name='" + name + "'"
        if len(self.__connectDb(sql)) >= 1:
            print('ERROR: This name already exites')
            return

        self.__name = name
        self.__containerCopies = containerCopies
        self.__image = image
        if(specifyNode == None):
            self.__specifyNode = self.__initNode()
        else:
            self.__specifyNode = specifyNode
        self.__comp = compType
        self.__compNum = compNum
        self.__compMemory = compMemory
        self.__createTime = datetime.datetime.strftime(
            datetime.datetime.now(), '%Y-%m-%d %H:%M:%S.%f')

        sql = "insert into `tasks`(`name`,`containerCopies`,"+ \
            "`imageList`, `specifyNode`,`compType`,`compNum`,"+ \
            "`compMemory`,`createTime`) values('" + name + "',"+ \
            str(containerCopies) + ",'" + image + "','" + \
            str(specifyNode) + "','" + compType + "'," + str(compNum) \
            + ",'" + compMemory + "','" + self.__createTime + "')"
        self.__connectDb(sql)

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

    def forSort(self):
        return self.__createTime

    # choose a suitable Node
    def __initNode(self):
        return
