import os

def ping(hostname):
    cmd = "ping -c 1 %s"%(hostname)\
            + " | grep icmp_seq"\
            + " | awk '{print $8}'" \
            + " | awk -F= '{print $2}'"
    retStr = os.popen(cmd).read()
    try:
        return float(retStr)
    except:
        return 0x7fff


if __name__ == "__main__":
    print(ping("baidu.com"))

