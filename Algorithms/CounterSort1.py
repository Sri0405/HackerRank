__author__ = 'sridhar'

from collections import  Counter

num =int(raw_input())
x = map(int,raw_input().rstrip().split(" "))
clist= Counter(x)
string= ""
for i in range(100):
    if i in clist:
        for k in range(clist[i]):
            string = string + str(i)+" "


print string