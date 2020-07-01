from Executor import Executor
import _thread

exe1 = Executor()
path = './test.yaml'

exe1.executeFile(path)
