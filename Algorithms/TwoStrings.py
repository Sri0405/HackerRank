__author__ = 'sridhar'

from collections import Counter
for i in range(int(raw_input())):
    c1= Counter(raw_input())
    c2= Counter(raw_input())
    found = "NO"
    for i in c1:
        if i in c2:
            found ='YES'

    print found