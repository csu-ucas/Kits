//
// Created by 韩佳蓉 on 2020-03-05.
//

#ifndef MYSERVER_THREADPOOL_H
#define MYSERVER_THREADPOOL_H

#include <vector>
#include <queue>
#include <thread>
#include <mutex>
#include <functional>
#include <condition_variable>//条件变量，通知实现线程同步

namespace myserver{

class ThreadPool{

public:
    using JobFunction = std::function<void()>;

    ThreadPool(int numWorkers);
    ~ThreadPool();
    void pushJob(const JobFunction& job);

private:
    std::vector<std::thread> threads_;
    std::mutex lock_;
    std::condition_variable cond_;
    std::queue<JobFunction> jobs_;
    bool stop_;

};
}

#endif //MYSERVER_THREADPOOL_H
