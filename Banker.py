import numpy as np


class ProcessError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Banker(object):
    def __init__(self, process_size, res_size):
        self.process_size = process_size  # 进程数量
        self.res_size = res_size  # 资源类数

        self.Available = []  # 当前各资源可用数量
        self.Max = {}  # 最大需求矩阵
        # 初始化最大需求矩阵
        for i in range(0, self.process_size):
            self.Max["p{}".format(i)] = []
        self.Allocation = {}  # 已分配资源矩阵
        for i in range(0, self.process_size):
            self.Allocation["p{}".format(i)] = []
        self.Need = {}  # 当前需求矩阵
        for i in range(0, self.process_size):
            self.Need["p{}".format(i)] = []
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
        pro_index = process[1]
        self.Request[pro_index] = request
        print(self.Request)

        for i in range(0, self.res_size):
            if self.Request[pro_index][i] > self.Need[pro_index][i]:
                raise ProcessError("{}进程申请的[{}]资源超出了其需求".format(pro_index, i))
            if self.Request[pro_index][i] > self.Available[i]:
                raise ProcessError("{}进程申请的[{}]资源超出了当前系统的资源可用数".format(pro_index, i))
        temp_Avaliable = self.Available
        temp_Need = self.Need
        temp_Allocation = self.Allocation

        for i in range(0, self.res_size):
            temp_Avaliable[i] -= self.Request[pro_index][i]
            temp_Need[pro_index][i] += self.Request[pro_index][i]
            temp_Allocation[pro_index][i] -= self.Request[pro_index][i]
        # 进行安全性检查
        if self.checkProcessMatrixSafe(temp_Avaliable, temp_Allocation, temp_Need):
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

        for i in range(0, self.process_size):
            if Finish[i] is True:
                continue
            if Finish[i] is False and checkNeedRight(temp_Need["P{}".format(i)], Work, self.res_size):
                print("find P{}".format(i) + "is safe")
                for j in range(0, self.res_size):
                    Work[j] += self.Allocation["P{}".format(i)][j]
                Finish[i] = True

                
