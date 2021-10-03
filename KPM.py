#建立NEXT数组

def buildNext(x:str):
    next=[]
    next.append(0)
    for i in x[1:]:
        if (next[i-1] == 0) and x[i] == x[1]:
            next.append(1)
        elif next[i-1] == 0 and x[i] != x[1]:
            next.append(0)
        elif next [i-1] !=0:
            if x[i] == x[next[i-1]]:
                next[i].append(next[i-1]+1)
            else:
                if x[i] == x[1]:
                    next.append(1)
                else:
                    next.append(0)
    return next


aa = "abcabd"
kk = buildNext(aa)
print(kk)
