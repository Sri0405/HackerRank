__author__ = 'sridhar'

from collections import Counter
import math

for i in range(int(raw_input())):
    raw_input()
    counter = Counter(raw_input().rstrip().split())
    count =0
    for key,val in counter.iteritems():
        if(val>1):
            count+= val*(val-1)

    print count