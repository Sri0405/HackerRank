__author__ = 'sridhar'

from collections import Counter

for i in range(int(raw_input())):
    str= raw_input()
    if(str.__len__()%2==1):
        print -1
    else:
        count =0
        # print str[str.__len__()/2:]
        # print str[:str.__len__()/2]
        l2 =Counter(str[str.__len__()/2:])
        l1 =Counter(str[:str.__len__()/2])
        # print l1
        # print l2
        for i in (l2):
            if l2[i] - l1.get(i,0) > 0:
                count += l2[i] - l1.get(i,0)
        print count