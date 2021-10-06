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
    next_str = buildNext(x)
    flag = 0
    while(i<len(sstr)):
        while(j<len(x)):
            if j<len(x) and i+j<len(sstr) and sstr[int(i+j)] == x[int(j)] :
                j+=1
            else:
                #不等的话就跳转
                i = i+(j-1)-(next_str[j]-1)
                flag = (j-1)-(next_str[j]-1)
                j=0
                break
        if(j==len(x)):
            res.append(i)
            j=0
            flag=0
        if flag == 0:
            i+=1
            flag = 0
    return res

strr = "piggippppig"
aa = search(strr, "pig")
print(aa)



