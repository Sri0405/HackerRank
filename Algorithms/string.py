# Panagram and not Panagram
import collections

b = map(str, raw_input().rstrip().lower())
d = collections.defaultdict(int)
for i in b:
    if i != ' ':  # exclude spaces
        d[i] += 1

print d
print d.__len__()
if (d.__len__()) == 26:
    print "panagram"
else:
    print "not panagram"
