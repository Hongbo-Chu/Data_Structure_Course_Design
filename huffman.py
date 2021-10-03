#先统计词频用hashmap
import collections as cl
def freq(q:str):
    di = cl.Counter(q)
    return di

#hash map 的实现