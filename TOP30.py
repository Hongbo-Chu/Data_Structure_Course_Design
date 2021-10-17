#利用倒排索引实现top30
#暂未开发范围选定功能

from collections import defaultdict
import os
class daopai:
    def __init__(self):
        self.indexx ={}
        self.liss = defaultdict(int)#用于存放倒排索引
        # self.wordLis = defaultdict(int)#在每一篇文章中建立关键词字典来记录出现了多少次# #会不停的变化

        files_path = 'cs_data'
        dirs = os.listdir(files_path)
        for file in dirs:
            path = (files_path + '\\' + file)

            with open(path) as f:#去除标点
                data = f.read()
                for i in ',.:?><"!\/':
                    data = data.replace(i, "")


                buf = ""

                for i in range(len(data)):
                    if (data[i] != " "):
                        buf += data[i]
                    else:
                        self.liss[buf] +=1
                        buf = ""

        self.indexx = dict(self.liss)
        self.indexx = sorted(self.indexx.items(), key=lambda item: item[1],reverse=True)
        i =1
        for key in self.liss:
            print("第%d多:"%i)
            i+=1
            print(key)
            if i>=30:
                break

    def getInv(self):
        return self.indexx

a = daopai()