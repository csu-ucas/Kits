import os

import docker
import yaml

class Executer: 
    def __init__(self):
        pass

    def executeFile(self, filePath):
        try:
            f = open(filePath, 'r', encoding='utf-8')
            data = f.read()
            f.close()
        except IOError:
            print("Error: 没有找到文件或读取文件失败")

        try:
            data = yaml.load(data, Loader=yaml.Loader)
        except yaml.YAMLError as exec:
            print('Error in data:')
            if hasattr(exc, 'problem_mark'):
                mark = exc.problem_mark
                print("Error position: (%s:%s)" % (mark.line + 1, mark.column + 1))

        if (type(data).__name__ == 'dict') and ('type' in data.keys()) and (data['type'] == 'container'):
            self.container(data)
        elif (type(data).__name__ == 'dict') and ('type' in data.keys()) and (data['type'] == 'image'):
            self.image(data)
        else:
            print('Please lable right type in yaml file')

    def container(self, data):
        para = ''
        if 'act' not in data.keys():
            print('Please lable right act in yaml file')
            return
        for i, key in enumerate(data['act'].keys()):
            if key == 'opt':
                continue
            if key=='name' and (data['act']['opt'] == 'start' or data['act']['opt'] == 'stop'):
                continue
            para += key
            para += '='
            if type(data['act'][key]).__name__ == 'str':
                para += '"' + str(data['act'][key]) + '"'
            else:
                para += str(data['act'][key])
            if i + 1 != len(data['act']):
                para += ','
        try:
            client = docker.from_env()

            if data['act']['opt'] == 'start' or data['act']['opt'] == 'stop':
                st = 'client.containers.get(container_id =%s)' % ('"'+data['act']['name']+'"')
                container=eval(st)
                st = 'container.%s(%s)' % (data['act']['opt'],para)
            else:
                st = 'client.containers.%s(%s)' % (data['act']['opt'], para)

            res = eval(st)
            
            if data['act']['opt'] in ['create','run','start','stop']:
                print('%s sucessfully' % data['act']['opt'])
                return '%s sucessfully' % data['act']['opt']
            else:
                for i in res:
                    print(i.id[:8],i.image,i.name,i.status)
                return res
        except (docker.errors.DeprecatedMethod,docker.errors.ContainerError,docker.errors.NotFound, docker.errors.ImageNotFound, docker.errors.APIError,TypeError ) as e:
            print('数据错误:',e)

    def image(self, data):
        para = ''
        for i, key in enumerate(data['act'].keys()):
            if key == 'opt':
                continue
            para += key
            para += '='
            if type(data['act'][key]).__name__ == 'str':
                para += '"' + str(data['act'][key]) + '"'
            else:
                para += str(data['act'][key])
            if i + 1 != len(data['act']):
                para += ','

        try:
            client = docker.from_env()
            st = 'client.images.%s(%s)' % (data['act']['opt'], para)
            res = eval(st)
            if data['act']['opt'] == 'pull' or data['act']['opt'] == 'push':
                print('%s sucessfully' % data['act']['opt'])
                return '%s sucessfully' % data['act']['opt']
            else:
                for i in res:
                    print(i.id,i.tags)
                return res
        except (docker.errors.DeprecatedMethod,docker.errors.ContainerError,docker.errors.NotFound, docker.errors.ImageNotFound, docker.errors.APIError,TypeError) as e:
            print('数据错误:',e)
