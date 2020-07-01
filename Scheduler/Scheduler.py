from Task.Task import Task


class Scheduler:
    # init
    def __init__(self):
        pass

    # sort Task
    def sort_Task(self, taskList):
        taskList = sorted(taskList, key=lambda Task: Task.createTime, reverse=True)
        return taskList
