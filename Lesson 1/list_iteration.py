
#判断是否可以迭代，是否是迭代器
from collections import Iterable,Iterator
print(isinstance ('abcde',Iterable))
print(isinstance ('abcde',Iterator))

#list的迭代1
list = ['html', 'js', 'css', 'python']
for i in list:
    print ("序号：%s   值：%s" % (list.index(i) + 1, i))
    print (i)
   # print(i.index)有问题
   # print(list[i]) 有问题

#list的迭代2
for i in range(len(list)):
    print("序号:%s    值:%s" %(i+1,list[i]))

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def MaxMinSearch(L):
    t    = L[0]
    tmax = L[0]
    tmin = L[0]
    for t in L:
        if t>tmax:
            tmax=t
        elif t<tmin:
            tmin=t
    LL=[tmin,tmax]
    return LL
print(MaxMinSearch([1,2,3,44,66,32,44,21,43,4]))