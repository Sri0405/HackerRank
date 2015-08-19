__author__ = 'sridhar'

from collections import Counter
str1= raw_input()
str2= raw_input()

if(str1.__len__()>str2.__len__()):
    c1= Counter(str1)
    c2= Counter(str2)
else:
    c1= Counter(str2)
    c2= Counter(str1)

# print c1
# print c2
count =0

for i in c1:
    if i in c2:
        # print i,"this is in ", "+",c1[i]-c2[i]
        count+= abs(c1[i]-c2[i])
        del c2[i]
    else:
        # print i," this is not in ", c1[i]
        count+=c1[i]

# print c2, "this is c2"
for i in c2:
    count+=c2[i]


print count