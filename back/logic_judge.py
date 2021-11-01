"""
用于接收和处理逻辑表达式
"""

import os
from collections import defaultdict

class logicSearch:
    def __init__(self, input:str, invidx:dict):
        self.invidx = invidx
        self.prefix = input
        #获得文件名列表
        files_path = 'cs_data'
        dirs = os.listdir(files_path)
        self.ansList = []
        for file in dirs:
            self.ansList.append(file)  #初始化答案文件列表

    def __and__(self, other:list):
        # 通过hashtable将N^2复杂度变为N+1
        aa = defaultdict(int)
        for it in self.ansList:
            aa[it] = 1

        for it in other:
            if aa[it] != 0:
                aa[it] += 1
        self.ansList =[]#清空旧表
        for ite in aa:
            if aa[ite] == 2:
                self.ansList.append(ite)
        return self.ansList

    def __or__(self, other):
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

    def getAns(self):
        #后缀表达式求职
        wordList = []
        # self.ansList = fileList
        for item in self.suffix:
            if item == "&":
                temp1 = wordList[-1]
                wordList.pop(-1)
                temp2 = wordList[-1]
                wordList.pop(-1)
                self.ansList =self.ansList & (temp1 & temp2)
            elif item == "|":
                temp1 = wordList[-1]
                wordList.pop(-1)
                temp2 = wordList[-1]
                wordList.pop(-1)
                self.ansList = self.ansList & (temp1 | temp2)
        return self.ansList



    def preToSuf(self):#前缀转后缀
        outputStack = []
        opStack = []
        buf = ""#用来读单词的
        for i in self.prefix:
            if (i == "&") or (i == "|") or (i == "(") or (i == ")"):
                if buf != "":
                    outputStack.append(buf)
                buf = ""
                if i != ")":
                    opStack.append(i)
                elif i == ")":
                    for op in range(len(opStack)):
                        if opStack[op] == "(":
                            opStack.pop(-1)
                            break
                        outputStack.append(opStack[-1])
                        opStack.pop(-1)
            else:
                buf += i
        if len(buf)!=0:
            outputStack.append(buf)
        for op in range(len(opStack)):#最后剩下的
            outputStack.append(opStack[-1])
            opStack.pop(-1)
        self.suffix = outputStack
        # return outputStack



strr = "lo&((cn|dd)&ss)&dsd"
a = logicSearch(strr)
b = a.preToSuf()
print(b)







from collections import defaultdict
class test :
    def __init__(self):
        self.x = ["ac", "as"]
        self.y = ["ee", "ww","123"]
        self.ans = []
    def __and__(self, other, x):
        #通过hashtable将N^2复杂度变为N+1
        aa = defaultdict(int)
        for it in self.y:
            aa[it] = 1
        for it in other:
            if aa[it] !=0:
                aa[it] += 1
        for it in x:
            if aa[it] !=0:
                aa[it] += 1
        for ite in aa:
            if aa[ite] >= 2:
                self.ans.append(ite)
        return self.ans


kk = test()
ww = ["ee", "www",]
uu = [ "www","123"]
print()