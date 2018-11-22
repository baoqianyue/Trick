#7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1,请求页面队列#
def loadPage(filename):
    """读取文件中的页面"""
    f = open(filename)
    page = f.readline()
    return page

#先进先出算法FIFO#


def FIFO(filename, internal_num):
    """
    param internal_num:主存中的物理块数量
    """
    print("-------------------------------------FIFO-----------------------")
    page = loadPage(filename).split()
    totalNum = len(page)  # 总请求次数
    print(totalNum)
    internalMem = []  # 主存n个物理块
    notCount = 0  # 记录缺页数
    replaceCount = 0  # 置换次数
    for i in page:
        if i not in internalMem:
            print('当前页面申请:%s,引发缺页中断' % (i))
            notCount += 1
            if len(internalMem) < internal_num:  # 如果internalMem中没有放满
                internalMem.append(i)
                print('当前内存中物理块情况:')
                print(internalMem)
            else:
                replaceCount += 1
                print('换出页面:%s' % (internalMem[0]))
                internalMem[:internal_num - 1] = internalMem[1:internal_num - 1]
                print('换入页面:%s' % (i))
                internalMem.append(i)
                print('当前内存中物理块情况:')
                print(internalMem)
        else:
            print('此次请求正常,无需中断')
    print("缺页数为:", notCount)
    print("置换次数为:", replaceCount)
    print("-------------------------------------FIFO----------------------")


#最近最久未使用算法LRU#
def LRU(filename, internal_num):
    """
    param internal_num:主存中的物理块数量
    """
    print("-------------------------------------LRU-----------------------")
    page = loadPage(filename).split()
    totalNum = len(page)  # 总请求次数
    internalMem = []  # 主存n个物理块
    notCount = 0  # 记录缺页数
    replaceCount = 0  # 置换次数
    flag = 0  # 标记是否缺页
    for i in page:  # 将要访问的列表元素进行循环
        if i not in internalMem:  # 如果要访问的元素不在page中 即为缺页
            print('当前页面申请:%s,引发缺页中断' % (i))
            notCount += 1
            flag = 1
            if len(internalMem) < internal_num:  # 如果internalMem中没有放满
                # 将当前页面加到内存队列尾部
                internalMem.append(i)
                print('当前内存中物理块情况:')
                print(internalMem)
            else:
                # 如果列表满了,将列表首元素换出
                # 同时其他页面提前,将新页面加到队尾
                replaceCount += 1
                print('换出页面:%s' % (internalMem[0]))
                internalMem[: internal_num - 1] = internalMem[1:]
                print('换入页面:%s' % (i))
                internalMem[internal_num - 1:] = [i]
                print('当前内存中物理块情况:')
                print(internalMem)
        else:  # i元素在列表中,不会中断
            flag = 0
            print('当前页面申请:%s,需移动队列维护LRU关系' % (i))
            # 将该页面移动到队尾,其他依次前移
            internalMem[internalMem.index(
                i):] = internalMem[internalMem.index(i)+1:]
            internalMem.append(i)  # 将i元素插入到移动后的列表后面
            print('当前内存中物理块情况:')
            print(internalMem)
    print("缺页数为:", notCount)
    print("置换次数为:", replaceCount)
    print("-------------------------------------LRU----------------------")


if __name__ == "__main__":
    FIFO('C:/Users/鲍骞月/Desktop/request.txt', 3)
    LRU('C:/Users/鲍骞月/Desktop/request.txt', 3)
