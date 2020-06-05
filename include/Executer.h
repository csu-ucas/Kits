#ifndef EXECUTER_H
#define EXECUTER_H


class Executer
{
    public:
        Executer();
        virtual ~Executer();

    protected:
        //Waiting Deploying Feedback Error
        string State;

        //认证
        void Login(string username,string password);
        void Login(string username,string password,string email);
        void Login(string username,string password,string email,string serveraddress);


        //查询
        //查询所有
        string ListContainers(bool all,int limit,int Size);
        //查询容器运行的进程
        string GetRunningContainers(string id,string ps_args);

        //新增
        //新建Container
        string StartContainer(string id);

        //修改
        //更新Container
        string UpdateContainer(string id);
        //重启Container
        string RestartContainer(string id,int t);
        //暂停Container
        string PauseContainer(string id);
        //恢复Container
        string UnpauseContainer(string id);


        //删除
        //停止并删除Container
        string StopContainer(string id,int t);
        //删除Container
        string KillContainer(string id);

    private:
};

#endif // EXECUTER_H
