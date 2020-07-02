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

    # run one task using Executor
    def excuteTask(self, task):
        a = 1
        yml = {}
        yml['type'] = 'container'
        while a <= task._Task__containerCopies:
            yml['act'] = {'opt': 'run', 'image': task._Task__image,
                          'name': task._Task__name + '_' + str(a),
                          'mem_limit': str(task._Task__compMemory),
                          'detach': True}
                          
            curpath = os.path.dirname(os.path.realpath(__file__))
            yamlPath = os.path.join(curpath, "run.yaml")
                        
            with open(yamlPath, mode='w', encoding='utf-8') \
                    as file:
                yaml.dump(yml, file, Dumper=yaml.RoundTripDumper)
            executor = Executor()
            executor.executeFile(yamlPath)
            a += 1

    # sort tasks by createTime
    def sortedTask(self, taskList):
        taskList = sorted(taskList, key=Task.forSort)
        return taskList


if __name__ == '__main__':

    # run one task
    Task._Task__connectDb(Task, "delete from " + \
                          "tasks where name=\'task_test\'")
    task1 = Task('task_test', 2, 'ubuntu', 6, \
                 'CPU', 1, '100m')
    scheduler = Scheduler()
    scheduler.excuteTask(task1)

    # run one or more tasks
    '''
    Task._Task__connectDb(Task,"delete from "+ \
                        "tasks where name=\'task_test1\'")
    Task._Task__connectDb(Task,"delete from "+ \
                        "tasks where name=\'task_test2\'")
    tasks=[]
    tasks.append(Task('task_test1',2,'ubuntu' \
                ,6,'CPU',1,'100m'))
    tasks.append(Task('task_test2',2,'ubuntu' \
                ,6,'CPU',1,'100m'))
    scheduler=Scheduler()
    tasks=scheduler.sortedTask(tasks)
    for task in tasks:
        print(task._Task__createTime)
        scheduler.excuteTask(task)
    '''
