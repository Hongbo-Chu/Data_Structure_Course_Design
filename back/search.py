# ww = input("输入要查找的字符")
# with open("cs_data/0_3.txt", "r") as f:
#     data = f.read()
#     print(data.find(ww))
import os
import KMP
import json
from logic_judge_final import logicSearch
from Inverted_index import daopai
from collections import defaultdict
# ww = input("输入要查找的内容")
# files_path = 'Data_Structure_Course_Design\cs_data'
# dirs = os.listdir(files_path)
# for file in dirs:
#     path = (files_path+'\\'+file)
#     with open(path) as f:
#         data = f.read()
#         temp = KMP.search(data, ww)
#         if temp != []:
#             print("在"+file+"中发现" + ww+" 出现在这些位置:")
#             print(temp)
def searcher(x:str) ->json:
    #更改为逻辑搜索
    a = daopai().getInv()
    try:
        b =  logicSearch(x,a)
        anslist = b.getAns()#里面是文件名的list
    except KeyError:
        print("当前条件下找不到匹配文件！")
    #将要搜索的词挑出来
    words = []
    buf = ""
    for i in x:
        if (i == "&") or (i == "|") or (i == "~"):
            if buf != "":
                words.append(buf)
            buf = ""
            words.append(i)
        else:
            buf += i
    words.append(buf)
    for i in ['|',"&"]:
        for k in words:
            if k == i:
                words.remove(i)
    cont = len(words)
    i = 0
    while i<cont:
        if words[i] == "~":
            del(words[i])
            del(words[i])
            i -= 2
        i += 1
        cont = len(words)
    
    
    files_path = 'D:\\vscodePythonSpace\Data_Structure_Course_Design\cs_data'
    final_ans = defaultdict(list)
    #先将x变为
    for file in anslist:
        path = (files_path+'\\'+file)
        #现在的搜索变为多词搜索
        #返回值为filename+句子
        with open(path) as f:
            data = f.read()
            for word in words:
                temp = KMP.search(data, word)
            #temp是list
                if temp != []:
                    final_ans[file].append(temp)
    jans = json.dumps(final_ans)
    return jans

# ww = input("输入要查找的内容")
# print(searcher(ww))   