#磁道请求队列:
# 100
#55 58 39 18 90 160 150 38 184#
def loadRequest(filename):
    f = open(filename)
    curr = f.readline()
    request = f.readline()
    return curr, request

#先来先服务算法-----------------------FCFS------------------#


def FCFS(filename):
    print('--------------FCFS------------------')
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

#最短寻道距离优先--------------------SSTF--------------------#


def findMinLengthIndex(curr, request):
    lengths = []  # 保存全部寻道长度
    for r in request:
        length = abs(int(curr) - int(r))
        lengths.append(length)
    minIndex = lengths.index(min(lengths))  # 返回距离当前磁道最近的磁道的索引
    return minIndex


def SSTF(filename):
    print('--------------SSTF------------------')
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

#扫描算法-------------------------SCAN---------------------#


def loadNext(now, next):
    length = abs(int(now) - int(next))
    print(next, length)
    return length


def findNext(now, data):
    biggerList = []
    smallerList = []
    for d in data:
        if int(d) > int(now):
            biggerList.append(d)
    if (len(biggerList) == 0):
        if len(data) != 0:
            for d2 in data:
                if int(d2) < int(now):
                    smallerList.append(d2)
            return max(smallerList)
        else:
            return None
    return min(biggerList)


def SCAN(filename):
    print('--------------SCAN------------------')
    length = 0  # 总寻道长度
    curr, request = loadRequest(filename)
    n = len(request.split())  # 计算请求磁道数,计算平均寻道时间
    request_copy = request.split().copy()
    for r in request_copy:
        next = findNext(curr, request_copy)
        if next == None:
            break
        length += loadNext(curr, next)
        print("当前磁道:%s, 下一磁道:%s" % (curr, r))
        curr = next
        request_copy.remove(next)
    print('平均寻道时间:%.1f' % (length / n))

#循环扫描算法---------------CSCAN------------------#


def cfindNext(now, data):
    biggerList = []
    smallerList = []
    for d in data:
        if int(d) > int(now):
            biggerList.append(d)
    if (len(biggerList) == 0):
        if len(data) != 0:
            now = 0
            return(findNext(now, data))
        else:
            return None
    return min(biggerList)


def CSCAN(filename):
    print('--------------CSCAN------------------')
    length = 0  # 总寻道长度
    curr, request = loadRequest(filename)
    n = len(request.split())  # 计算请求磁道数,计算平均寻道时间
    request_copy = request.split().copy()
    for r in request_copy:
        next = findNext(curr, request_copy)
        if next == None:
            break
        length += loadNext(curr, next)
        print("当前磁道:%s, 下一磁道:%s" % (curr, r))
        curr = next
        request_copy.remove(next)
    print('平均寻道时间:%.1f' % (length / n))


if __name__ == "__main__":
    FCFS('C:/Users/鲍骞月/Desktop/diskrequest.txt')
    SSTF('C:/Users/鲍骞月/Desktop/diskrequest.txt')
    SCAN('C:/Users/鲍骞月/Desktop/diskrequest.txt')
    CSCAN('C:/Users/鲍骞月/Desktop/diskrequest.txt')
