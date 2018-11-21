def loadPage(filename):
    """读取文件中的页面"""
    f = open(filename)
    page = f.readline()
    return page


def LRU(filename):
    page = loadPage(filename)
    internalMem = []  # 主存3个物理块
    notCount = 0  # 记录缺页数
    replaceCount = 0  # 置换次数
    flag = 0  # 标记是否缺页
    for i in page:  # 将要访问的列表元素进行循环
        if i not in internalMem:  # 如果要访问的元素不在page中 即为缺页
            print('当前页面申请:%s,引发缺页中断' % (i))
            notCount += 1
            flag = 1
            if len(internalMem) < 3:  # 如果internalMem中没有放满
                # 将当前页面加到内存队列尾部
                internalMem.append(i)
                print(internalMem)
            else:
                # 如果列表满了,将列表首元素换出
                # 同时其他页面提前,将新页面加到队尾
                replaceCount += 1
                print('换出页面:%s' % (internalMem[0]))
                internalMem[:2] = internalMem[1:]
                print('换入页面:%s' % (i))
                internalMem[2:] = [i]
                print(internalMem)
        else:  # i元素在列表中,不会中断
            flag = 0
            print('当前页面申请:%s,需移动队列维护LRU关系' % (i))
            # 将该页面移动到队尾,其他依次前移
            internalMem[internalMem.index(
                i):] = internalMem[internalMem.index(i)+1:]
            internalMem.append(i)  # 将i元素插入到移动后的列表后面
            print(internalMem)
    print("缺页数为:", notCount)
