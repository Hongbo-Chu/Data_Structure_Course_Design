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
        #self.codes = range(1)#用于存放编码
        self.codes = []
        self.b = [0]*10
       # self.flag = False
        #print(self.Huffbuf[0].value)


    # def encoding(self, root:node, flag:bool):
    #     #左零右一tlr
    #     if root != None:
    #         if root.name != '@':
    #             print(root.name+':'+aa(self.stack))
    #         elif flag==False:
    #             self.stack.append(0)
    #             print(self.stack)
    #         elif flag == True:
    #             self.stack.pop(-1)
    #             self.stack.pop(-1)
    #             self.stack.append(1)
    #             print(self.stack)
    #         self.encoding(root.left, False)
    #         #证明左边数完了改到右边了
    #         self.stack.pop(-1)
    #         self.stack.append(1)
    #         print(self.stack)
    #         print("ww")
    #         self.encoding(root.right, True)
    #         #能到这里说明向右走结束了

    #非递归前序遍历实现
    # def encoding(self):
    #     tt = self.Root
    #     stack = []
    #     code_stack = []
    #     while tt!=None or len(stack) != 0:
    #         if tt!=None:
    #             code_stack.append(list(self.codes))
    #             if tt.left!=None:
    #                 stack.append(tt)
    #                 self.codes.append(0)
    #
    #             if tt.name!='@':
    #                 print(tt.name+':'+aa(self.codes))
    #             tt=tt.left
    #         else:
    #             tt = stack[len(stack)-1]
    #             stack.pop(-1)
    #             self.codes = code_stack[len(code_stack)-1]
    #             code_stack.pop(-1)
    #             self.codes.pop(-1)
    #             self.codes.append(1)
    #             tt=tt.right
    #             # self.codes.append(1)


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
