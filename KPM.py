#建立NEXT数组
import numpy as np
def buildNext(x:str):
    next=np.zeros(len(x))
    next[0]=0
    #print(type(next[1]))
    i=1
    while(i<len(x)):
        if (next[i-1] == 0) and x[i] == x[0]:
            next[i] = 1
        elif next[i-1] == 0 and x[i] != x[0]:
            next[i] = 0
        elif next [i-1] !=0:
            if x[i] == x[int(next[i-1])]:
                next[i] = next[i-1]+1
            else:
                if x[i] == x[0]:
                    next[i] = 1
                else:
                    next[i] = 0
        i+=1
    return next

def search(sstr:str, x:str):#x是子串
    res=[]#用于存放答案
    i=0#原串指针
    j=0#子串指针
    next_str = buildNext(sstr)
    while(i<len(sstr)):
        while(j<len(x)):
            if sstr[int(i+j)] == x[int(j)]:
                j+=1
            else:
                #不等的话就跳转
                i = i+(j-1)-(next_str[j]-1)
                j=0
                break
        if(j==len(x)):
            res.append(i)
            j=0
        i+=1
    return res

strr = "imapigpig"
aa = search(strr, "pig")
print(aa)



