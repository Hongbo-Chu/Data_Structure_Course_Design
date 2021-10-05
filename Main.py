# ww = input("输入要查找的字符")
# with open("cs_data/0_3.txt", "r") as f:
#     data = f.read()
#     print(data.find(ww))

import os
ww = input("输入要查找的字符")
files_path = 'cs_data'
dirs = os.listdir(files_path)
for file in dirs:
    path = (files_path+'\\'+file)
    with open(path) as f:
        data = f.read()
        if (-1 != data.find(ww)):
            print("在"+file+"中发现"+ww)
