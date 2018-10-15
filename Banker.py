class ProcessError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Banker(object):
    def __init__(self, process_size=4, res_size=3):
        self.process_size = process_size  # 进程数量
        self.res_size = res_size  # 资源类数

        self.Available = []  # 当前各资源可用数量
        self.Max = {}  # 最大需求矩阵
        # 初始化最大需求矩阵
        for i in range(0, self.process_size):
            self.Max["P{}".format(i)] = []
        self.Allocation = {}  # 已分配资源矩阵
        for i in range(0, self.process_size):
            self.Allocation["P{}".format(i)] = []
        self.Need = {}  # 当前需求矩阵
        for i in range(0, self.process_size):
            self.Need["P{}".format(i)] = []
        self.Request = {}  # 请求资源矩阵
        for i in range(0, self.process_size):
            self.Request["P{}".format(i)] = []

    def getNeed(self):
        """
        计算需求矩阵
        :return:
        """
        for i in range(0, self.process_size):
            for j in range(0, self.res_size):
                self.Need["P{}".format(i)].append(
                    # 将Max和Allocation两个矩阵对应位置上的值相减
                    self.Max["P{}".format(i)][j] - self.Allocation["P{}".format(i)][j]
                )
                if self.Need["P{}".format(i)][j] < 0:
                    print("P{} Need Mat{} Error".format(i, j))

    def sendRequest(self, process, request):
        """
        请求资源
        :param process: 进程个体，eg:P1,P2...
        :param request: 资源请求向量
        :return:
        """
        self.Request[process] = request
        print(self.Request)

        for i in range(0, self.res_size):
            if self.Request[process][i] > self.Need[process][i]:
                raise ProcessError("{}进程申请的[{}]资源超出了其需求".format(process, i))
            if self.Request[process][i] > self.Available[i]:
                raise ProcessError("{}进程申请的[{}]资源超出了当前系统的资源可用数".format(process, i))
        temp_Avaliable = self.Available
        temp_Need = self.Need
        temp_Allocation = self.Allocation

        for i in range(0, self.res_size):
            temp_Avaliable[i] = temp_Avaliable[i] - self.Request[process][i]
            temp_Need[process][i] = temp_Need[process][i] - self.Request[process][i]
            temp_Allocation[process][i] = temp_Allocation[process][i] + self.Request[process][i]
        # 进行安全性检查
        if self.checkProcessMatrixSafe(temp_Avaliable, temp_Allocation, temp_Need) is True:
            print("安全检查通过, 系统状态发生变化")
            self.Available = temp_Avaliable
            self.Allocation = temp_Allocation
            self.Need = temp_Need
        else:
            print("Not safe, please wait")

    def checkProcessMatrixSafe(self, temp_Avaliable, temp_Allocation, temp_Need):
        """
        进行进程请求安全检查
        :param temp_Avaliable:
        :param temp_Allocation:
        :param temp_Need:
        :return:
        """

        def checkNeedRight(need_Pn, work, res_size):
            flag = True
            for i in range(0, res_size):
                if need_Pn[i] > Work[i]:
                    flag = False
            return flag

        Work = temp_Avaliable
        Finish = [False] * self.process_size
        SafeList = []

        for i in range(0, self.process_size):
            if Finish[i] is True:
                continue
            if Finish[i] is False and checkNeedRight(temp_Need["P{}".format(i)], Work, self.res_size):
                print("find P{}".format(i) + "is safe")
                for j in range(0, self.res_size):
                    Work[j] = Work[j] + self.Allocation["P{}".format(i)][j]
                Finish[i] = True
                SafeList.append("P{}".format(i))
                print(Work)

                for j in range(0, i):
                    if Finish[j] is True:
                        continue
                    if Finish[j] is False and checkNeedRight(temp_Need["P{}".format(j)], Work, self.res_size):
                        print("find P{}".format(j) + "is safe")
                        for k in range(0, self.res_size):
                            Work[k] = Work[k] + self.Allocation["P{}".format(j)][k]
                        Finish[j] = True
                        SafeList.append("P{}".format(j))
                        print(Work)

            if Finish == [True] * self.process_size:
                return True
            else:
                return False

    def exampleInit1(self):
        self.Available = [1, 1, 2]
        self.Max = {
            "P0": [3, 2, 2],
            "P1": [6, 1, 3],
            "P2": [3, 1, 4],
            "P3": [4, 2, 2]
        }
        self.Allocation = {
            "P0": [1, 0, 0],
            "P1": [5, 1, 1],
            "P2": [2, 1, 1],
            "P3": [0, 0, 2]
        }
        self.getNeed()


def example1():
    try:
        Bancker = Banker()
        Bancker.exampleInit1()
        Bancker.sendRequest("P1", [1, 0, 1])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    banker = Banker()
    banker.exampleInit1()
    banker.sendRequest("P1", [1, 0, 1])
