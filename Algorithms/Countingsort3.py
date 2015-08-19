__author__ = 'sridhar'

from collections import Counter
arr = []

for i in range(int(raw_input())):
    val = raw_input().rstrip().split()[0]
    arr.append(val)

# string= ' '.join(map(str,arr))

dict = Counter(arr)

print dict

count =0

str_t =''
for i in range(100):
    if dict.__contains__(str(i)):
        # print "contains " , i
        # print dict.get(i)
        count = count +int(dict.get(str(i)))

    str_t =str_t+str(count)+" "

print str_t