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


def findMinLengthIndex(curr, request):
    lengths = []  # 保存全部寻道长度
    for r in request:
        length = abs(int(curr) - int(r))
        lengths.append(length)
    minIndex = lengths.index(min(lengths))  # 返回距离当前磁道最近的磁道的索引
    return minIndex


def SSTF(filename):
    length = 0  # 总寻道长度
    queue = []
    curr, request = loadRequest(filename)
    request_copy = request.split().copy()
    n = len(request_copy)
    for r in request.split():
        index = findMinLengthIndex(curr, request_copy)  # 先找到最近磁道的索引
        sum = abs(int(curr) - int(request_copy[index]))
        length += sum
        queue.append(sum)
        print('当前磁道：%s, 下一磁道:%s, 移动:%d' % (curr, request_copy[index], sum))
        curr = request_copy[index]
        request_copy.remove(request_copy[index])
    print('平均寻道距离:%.f' % (length / n))


if __name__ == "__main__":
    FCFS('C:/Users/鲍骞月/Desktop/diskrequest.txt')
