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
    def __init__(self, x:str):

        self.Huffbuf =[node(val, key) for key, val in freq(x).items()]#创建Node列表
        self.Huffbuf.sort(key=lambda node: node.value, reverse=True)
        while len(self.Huffbuf)!=1:
            self.Huffbuf.sort(key= lambda node :node.value,reverse=True)
            temp = node(self.Huffbuf[-1].value+self.Huffbuf[-2].value, "@")
            temp.left = self.Huffbuf.pop(-1)
            temp.right = self.Huffbuf.pop(-1)
            self.Huffbuf.append(temp)
        self.Root = self.Huffbuf[0]#用于存放根节点
        self.codes = range(1)#用于存放编码
        print(self.Huffbuf[0].value)


    def encoding(self):

a = "abcd"
huffman(a)
