#include <string>
using namespace std;

struct Comp
{
    string type;//计算资源类型：CPU、FPGA、GPU
    int CompID;//计算资源序号
    float occupy;//已占用计算资源量
    float remain;//可用计算资源量
};

class NodeInfo {
public：
    int NodeID; //节点序号
    vector<int> PodIDList; //已部署的Pod序号列表
    vector<Comp>  CompIDList;// 计算资源序号列表
    int memory;//内存资源总量
    int memory_occcupy;//已用内存量
    int memory_remain;//剩余内存量
    int storage;//存储资源总量
    int storage_occupy;//已用存储量
    int storage_remain;//剩余存储量
    vector<int> UsedPortIDList;//已用端口列表
}

class TaskInfo {
public：
    int container_copies; //容器副本数
    vector<Image> ImageList; //所需镜像列表
    int specify_node; //指定调度节点（可选）
    string comp_type; //指定计算资源类型
    int comp_num;//指定计算资源数量
    int comp_memory;//指定内存资源数量
    int comp_storage;//指定存储资源数量
}

bool predicate(vector<NodeInfo> N,TaskInfo T,vector<int> &NL) //预选算法
{
    if T.specify_node!=0
        NL.push_back(specify_node);
    else
        for (int i = 0; i <N.size()-1; ++i) {
            for (int j = 0; i <N[i].Comp.size()-1; ++i) {
                if N[i].Comp[j].type==T.comp_type
                    int n=N[i].Comp[j].remain;
            }
            if n>=T.comp_num
                if N[i].memory_remain>=T.comp_memory && N[i].storage_remain>=T.comp_storage
                   NL.push_back(N[i]);
        }
    return ture;
}

int priority(vector<int> &NL, int a, int b, int c) //优选算法：负载均衡
{
    if NL.size()==1
        return NL[0].NodeID;
    else
    {
        double score[NL.size()];
        for (int i = 0; i <NL.size()-1; ++i) {
            score[i]=a*NL[i].storage_remain/NL[i].storage+b*NL[i].memory_remain/NL[i].memory;
            score_occupy=0;
            for (int j = 0; i <NL[i].Comp.size()-1; ++i) {
                score_occupy=NL[i].Comp[j].remain/(NL[i].Comp[j].remain+NL[i].Comp[j].occupy);
            }
            score[i]=score[i]+c*score_occupy;
        }
        return max_element(score.begin(), score.end())-score.begin();
    }
}
