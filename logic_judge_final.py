import os
from collections import defaultdict

class logicSearch:
    def __init__(self, input: str, invidx: dict):
        self.invidx = invidx
        self.Liss = []
        self.ansList = []
        buf =""
        for i in input:
            if (i == "&") or (i == "|"):
                self.Liss.append(buf)
                buf = ""
                self.Liss.append(i)
            else:
                buf +=i
        self.Liss.append(buf)
        print(self.Liss[1])
        # 获得文件名列表
        files_path = 'cs_data'
        dirs = os.listdir(files_path)

        for file in dirs:
            self.ansList.append(file)  # 初始化答案文件列表

    def Myand(self, other: list):
        # 通过hashtable将N^2复杂度变为N+1
        aa = defaultdict(int)
        for it in self.ansList:
            aa[it] = 1

        for it in other:
            if aa[it] != 0:
                aa[it] += 1
        self.ansList = []  # 清空旧表
        for ite in aa:
            if aa[ite] == 2:
                self.ansList.append(ite)
        return self.ansList

    def Myor(self, other:list):
        aa = {}
        for it in self.ansList:
            aa[it] = 0
        for it in other:
            aa[it] = 0
        self.ansList = []  # 清空旧表
        for ite in aa:
            self.ansList.append(ite)
        return self.ansList

    def getAns(self):
       # 第一项跟all&
        self.ansList = self.Myand(self.invidx[self.Liss[0]])
        self.Liss.pop(0)
        for ite in self.Liss:
            if len(self.Liss)>0:
                if ite=="&":
                    self.Liss.pop(0)
                    self.ansList = self.Myand(self.invidx[self.Liss[0]])
                    self.Liss.pop(0)
                else:
                    self.Liss.pop(0)
                    self.ansList = self.Myor(self.invidx[self.Liss[0]])
                    self.Liss.pop(0)
        return self.ansList
