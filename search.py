# ww = input("输入要查找的字符")
# with open("cs_data/0_3.txt", "r") as f:
#     data = f.read()
#     print(data.find(ww))
import os
import KPM
ww = input("输入要查找的内容")
files_path = 'cs_data'
dirs = os.listdir(files_path)
for file in dirs:
    path = (files_path+'\\'+file)
    with open(path) as f:
        data = f.read()
        temp = KPM.search(data, ww)
        if temp != []:
            print("在"+file+"中发现" + ww+" 出现在这些位置:")
            print(temp)