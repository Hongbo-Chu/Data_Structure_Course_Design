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
                for i in range(len(data)):
                    if (data[i] != " "):
                        buf += data[i]
                    else:
                        self.liss[buf].append(file)
                        i += 1
                        buf = ""
        self.indexx = dict(self.liss)
a = daopai()
print(a.indexx )
