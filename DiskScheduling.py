def loadRequest(filename):
    f = open(filename)
    curr = f.readline()
    request = f.readline()
    return curr, request


def FCFS(filename):
    length = 0  # 总寻道长度
    queue = []  # 寻道记录
    curr, request = loadRequest(filename)
    for r in request.split():
        sum = abs(int(curr) - int(r))
        length += sum
        queue.append(sum)
        print("当前磁道:%s, 下一磁道:%s, 移动:%d" % (curr, r, sum))
        curr = r
    n = len(request.split())  # 计算请求磁道数,计算平均寻道时间
    print('平均寻道时间:%.1f' % (length / n))


if __name__ == "__main__":
    FCFS('C:/Users/鲍骞月/Desktop/diskrequest.txt')
