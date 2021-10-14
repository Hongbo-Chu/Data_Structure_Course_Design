from collections import defaultdict
import os
class daopai:
    def __init__(self):
        self.indexx ={}
        self.liss = defaultdict(list)
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
                        i += 1
                        buf = ""
        self.indexx = dict(self.liss)
    def search(self, input:str):
        return self.liss[input]
a = daopai()
print(a.search("Time"))

