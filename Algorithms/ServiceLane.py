__author__ = 'sridhar'
# Service Lane Problem
N, T = map(int,raw_input().rstrip().split(" "))
Array = map(int, raw_input().rstrip().split(" "))

def find_min(start,end):
    min=Array[start]
    for i in range(start,end+1):
        # print start, end,"this"
        if(Array[i]<min):
            min = Array[i]
    return min


for i in range(T):
    for i in range(N):
        start, end = map(int,raw_input().rstrip().split(" "))
        print find_min(start,end)