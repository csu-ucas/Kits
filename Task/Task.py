from MasterVoter.Node import Node
import datetime

class Task:
    #init
    def __init__(self,containerCopies,imageList,specifyNode, \
                compType,compNum,compMemory,compStorage):
        self.__containerCopies=containerCopies
        self.__imageList=imageList
        if(specifyNode==None):
            self.__specifyNode=initNode()
        else:
            self.__specifyNode=(specifyNode)
        self.__compType=compType
        self.__compNum=compNum
        self.__compMemory=compMemory
        self.__compStorage=compStorage
        self.createTime=datetime.datetime.strftime( \
            datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
        

    #choose a suitable Node
    def __initNode():
        pass

