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
        self.codes = []
        self.b = [0]*10
    def pre(self,tree,length):
        node=tree
        if (not node):
            return
        elif node.name!='@':
            x = ''
            print (node.name + '的编码为:')
            for i in range(length):
                x+=str(self.b[i])
            print (x)
            print( '\n')
            return
        self.b[length]=0
        self.pre(node.left,length+1)
        self.b[length]=1
        self.pre(node.right,length+1)
     #生成哈夫曼编码
    def get_code(self):
        self.pre(self.Root,0)

def aa(nums:list) ->str:
    m = ''
    for i in range(len(nums)):
        x = str(nums[i])
        m+=x
    return m
a = "aaaaaaassdfffcc"
k = huffman(a)
k.get_code()
