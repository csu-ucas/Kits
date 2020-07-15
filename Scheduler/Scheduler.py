import sys
import os

# add father path to import Task and Executor
current_path = os.path.dirname(os.path.realpath(__file__))
fatherPath = os.path.abspath( \
                            os.path.dirname(current_path) \
                            + os.path.sep + ".")
sys.path.append(fatherPath)  

from Task.Task import Task
from Executor.Executor import Executor
from ruamel import yaml

class Scheduler:
    # init
    def __init__(self):
        pass
        

    # sort tasks by createTime
    def sortedTaskByTime(self, taskList):
        taskList = sorted(taskList, key=Task.forSortTime)
        return taskList

    # sort tasks by priority
    def sortedTaskByPriority(self, taskList):
        taskList = sorted(taskList, key=Task.forSortPriority)
        return taskList
    

if __name__ == '__main__':

    #task1
    yamlPaths=[]
    curpath = os.path.dirname(os.path.realpath(__file__))
    yamlPaths.append(os.path.join(curpath, "run1.yaml"))
    yamlPaths.append(os.path.join(curpath, "run2.yaml"))
    
    task1=Task('task1',1,yamlPaths,'CPU',1,'100m',2)

    #task2
    yamlPaths=[]
    curpath = os.path.dirname(os.path.realpath(__file__))
    yamlPaths.append(os.path.join(curpath, "run3.yaml"))
    yamlPaths.append(os.path.join(curpath, "run4.yaml"))
    
    task2=Task('task2',1,yamlPaths,'CPU',1,'100m',1)

    scheduler=Scheduler()
    tasks=[]
    tasks.append(task1)
    tasks.append(task2)
    tasks=scheduler.sortedTaskByPriority(tasks)
    for task in tasks:
        task.getContainers()
        print(task._Task__name)

