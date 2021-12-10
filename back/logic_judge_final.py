import os
from collections import defaultdict

from flask.helpers import send_file
from numpy.lib.function_base import select

class logicSearch:
    def __init__(self, input: str, invidx: dict):
        self.invidx = invidx #传入的倒排表
        self.Liss = []#存要找的序列
        self.ansList = []#存答案
        buf =""
        for i in input:
            if (i == "&") or (i == "|") or (i == "~"):
                if buf != "":
                    self.Liss.append(buf)
                buf = ""
                self.Liss.append(i)
            else:
                buf +=i
        self.Liss.append(buf)
        print("in logic")
        print(self.Liss)
        # 获得文件名列表  
        files_path = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\'
        dirs = os.listdir(files_path)

        for file in dirs:
            self.ansList.append(file)  # 初始化答案文件列表
    def Myand(self, other: list):
        # 通过"hashtable将N^2复杂度变为N+1
        aa = []
        for it in self.ansList:
            aa.append(it)
        self.ansList = []  # 清空旧表
        for ita in other:
            if ita in aa:
                self.ansList.append(ita)
        return self.ansList

    def Myor(self, other:list):
        aa = {}#自动覆盖重复的
        for it in self.ansList:
            aa[it] = 0
        for it in other:
            aa[it] = 0
        self.ansList = []  # 清空旧表
        for ite in aa:
            self.ansList.append(ite)
        return self.ansList
    #and的NOt是把anslist中含有这个词的删除
    #or的NOT是将all中不含这个词的添加到anslist中
    def Mynot_and(self, other:list):
        #把anslist中含有这个词的删掉
        aa = defaultdict(int)
        for it in self.ansList:
            aa[it] = 1
        for ita in other:
            if aa[ita] == 1:
                aa[ita] += 1
        self.ansList = []
        for itt in aa:
            if aa[itt] == 1:
                self.ansList.append(itt)
        return self.ansList
        
    def Mynot_or(self, other:list):
        files_path = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\'
        dirs = os.listdir(files_path)
        aa = []
        for file in dirs:
            aa.append(file)  # 初始化答案文件列表
        for it in other:
            aa.remove(it)
        for itt in aa:
            self.ansList.append(itt)
        return self.ansList
            
    def getAns(self):
        # 第一项跟all&
        self.ansList = self.Myand(self.invidx[str(self.Liss[0])])
        self.Liss.pop(0)
        for ite in range(len(self.Liss)):
            if len(self.Liss)>0:
                if self.Liss[0] == "&":
                    self.Liss.pop(0)
                    if self.Liss[0] == "~":
                        self.Liss.pop(0)
                        if not(str(self.Liss[0]) in self.invidx):#防治KEYerror
                            self.Liss.pop(0)
                            continue
                        self.ansList = self.Mynot_and(self.invidx[str(self.Liss[0])])
                        self.Liss.pop(0)                  
                        continue
                    if not(str(self.Liss[0]) in self.invidx):#防治KEYerror
                        self.Liss.pop(0)
                        self.ansList=[]
                        print("当前条件下找不到匹配文件！")
                        break                  
                    self.ansList = self.Myand(self.invidx[str(self.Liss[0])])
                    self.Liss.pop(0)                    
                elif ite == "|":
                    self.Liss.pop(0)
                    if self.Liss[0] == "~":
                        self.Liss.pop(0)
                        if not(str(self.Liss[0]) in self.invidx):#防治KEYerror
                            self.Liss.pop(0)
                            continue
                        self.ansList = self.Mynot_or(self.invidx[str(self.Liss[0])])
                        self.Liss.pop(0)                        
                        continue
                    if not(str(self.Liss[0]) in self.invidx):#防治KEYerror
                        self.Liss.pop(0)
                        continue
                    self.ansList = self.Myor(self.invidx[str(self.Liss[0])])
                    self.Liss.pop(0)                      
        return self.ansList


