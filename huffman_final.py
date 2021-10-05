#先统计词频用hashmap
import collections as cl

def freq(q:str) ->dict:
    di = cl.Counter(q)
    return di
#节点类
class node:
    def __init__(self, value: int, name):
        self.value = value
        self.name = name
        self.left = None
        self.right = None

class huffman:
    def __init__(self, path:str):
        with open(path) as f:
            x = f.read()
        self.Huffbuf =[node(val, key) for key, val in freq(x).items()]#创建Node列表
        self.Huffbuf.sort(key=lambda node: node.value, reverse=True)
        while len(self.Huffbuf)!=1:
            self.Huffbuf.sort(key= lambda node :node.value,reverse=True)
            temp = node(self.Huffbuf[-1].value+self.Huffbuf[-2].value, "@")
            temp.left = self.Huffbuf.pop(-1)
            temp.right = self.Huffbuf.pop(-1)
            self.Huffbuf.append(temp)
        self.Root = self.Huffbuf[0]#用于存放根节点
        self.codes = {}
        self.b = [0]*10

    def getFile(self, path) -> str:
        with open(path) as f:
            data = f.read()
        return data
    def encoding(self,tree,length):
        node=tree
        if (not node):
            return
        elif node.name!='@':
            x = ''
            # print (node.name + ':')
            for i in range(length):
                x+=str(self.b[i])
            temp = {node.name: x}
            self.codes.update(temp)
            # print (temp)
            # print( '\n')
            return
        self.b[length]=0
        self.encoding(node.left,length+1)
        self.b[length]=1
        self.encoding(node.right,length+1)
     #生成哈夫曼编码
    def get_code(self)-> dict:
        self.encoding(self.Root,0)
        return self.codes
    def encodingFile(self, path):
        data = self.getFile(path)
        newCoding=''
        for i in range(len(data)):
            newCoding+=self.codes[data[i]]
        print(newCoding)


path = "D:\\Data_Structure_Course_Design\\cs_data\\2_1.txt"
a = huffman(path)
a.get_code()
a.encodingFile(path)