from collections import defaultdict
import os
class daopai:
    def __init__(self):
        self.indexx ={}
        self.liss = defaultdict(list)#用于存放倒排索引
        # self.wordLis = defaultdict(int)#在每一篇文章中建立关键词字典来记录出现了多少次# #会不停的变化

        files_path = 'cs_data'
        dirs = os.listdir(files_path)
        for file in dirs:
            path = (files_path + '\\' + file)
            with open(path) as f:
                data = f.read()
                buf = ""
                flag = 0


                for i in range(len(data)):
                    if (data[i] != " "):
                        buf += data[i]
                    else:#处理一个词在一篇文章中出现多次的情况
                        for j in range(len(self.liss[buf])):
                            if self.liss[buf][j] != file:
                                flag +=1
                            else:
                                flag=0
                                break
                        if flag == len(self.liss[buf]):
                            self.liss[buf].append(file)
                        flag = 0
                        buf = ""


        self.indexx = dict(self.liss)


    def search(self, input:str):
        #此时已经有了倒排索引
        wordLis = defaultdict(int)  # 在每一篇文章中建立关键词字典来记录出现了多少次
        i = self.liss[input][2]
        self.topNum = {}
        for file in self.liss[input]:
            path = ('cs_data' + '\\' + file)
            with open(path) as f:
                data = f.read()
                buf = ""
                for i in range(len(data)):
                    if (data[i] != " "):
                        buf += data[i]
                    else:
                        wordLis[buf] += 1
                        buf = ""
                self.topNum[file] = wordLis[input]
                wordLis = defaultdict(int)
        self.topNum = sorted(self.topNum.items(), key=lambda item:item[1],reverse=True)
        print(self.topNum)


a = daopai()
a.search("story")

