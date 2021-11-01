from collections import defaultdict
import os
import logic_judge_final
"""
在原有的倒排索引的基础上添加了“TOP结果搜索”即：对于要搜索的单词进行在文章中出现的次数进行排序和统计
"""
class daopai:
    def __init__(self):
        self.indexx ={}
        self.liss = defaultdict(list)#用于存放倒排索引
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
    def getInv(self):
        return self.indexx
    def search(self, input:str):
        #此时已经有了倒排索引
        wordLis = defaultdict(int)  # 在每一篇文章中建立关键词字典来记录出现了多少次
        self.topNum = {}
        for file in self.liss[input]:
            path = ('cs_data' + '\\' + file)
            with open(path) as f:
                data = f.read()
                for i in ',.:?><"!\/':
                    data = data.replace(i, "")
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
        # print(self.topNum)
        return self.topNum


a = daopai().getInv()
print(a["man"])

# b = logic_judge_final.logicSearch("who&man",a)
# print(b.getAns())



# a = daopai().search("and")
# print(len(a))

