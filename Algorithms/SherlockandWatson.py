__author__ = 'sridhar'

from collections import deque

N,K,Q = raw_input().rstrip().split()
arr = deque(raw_input().rstrip().split())

arr.rotate(int(K))

for i in range(int(Q)):
    indx =int(raw_input())
    print arr[indx]

