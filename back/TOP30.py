#利用倒排索引实现top30
#暂未开发范围选定功能

from collections import Counter
import os
import json

class TOP:
    def __init__(self, flist:list) -> list:#输入是一个文件的列表
        self.flist = flist
        
    def sorrt(self):
        meaningless =["a", "A", "The", "the", "is", "are", "that", "this", "of", "in", "and", "or",
                      "it", "an", "to"
                      ]
        path1 = "D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data\\"
        alllis = []
        for fil in self.flist:
            fpath = path1+fil
            with open(fpath) as f:
                pasage = f.read()
                #去除标点
                for i in ',.:?><"!\/':
                    pasage = pasage.replace(i, "")
                buf = ""
                for i in range(len(pasage)):
                    # if pasage[i] == " ":
                    #     alllis.append(buf)
                    #     buf=""
                    # buf += pasage[i]
                    if pasage[i] != " ":
                        buf += pasage[i]
                    else:
                        alllis.append(buf)
                        buf = ""        
        res = Counter(alllis)
        
        L = sorted(res.items(),key=lambda item:item[1],reverse=True)
        #去除无意义的词：
        # for k in L: #TODO这个为啥不行捏 
        #     # print(k[0])
        #     if k[0] in meaningless:
        #         print("remove:"+k[0])
        #         # L.remove(k)
        
        for k in meaningless:
            for l in L:
                if l[0] == k:
                    L.remove(l) 
        L = L[:15]
        #转到字典
        dictdata = {}
        for l in L:
            dictdata[l[0]] = l[1]
        #再到json
        jres = json.dumps(dictdata)
        print(jres)
        return jres
    
ll = ["0_3.txt","1_1.txt"]
a = TOP(ll)
a.sorrt()       

        