# Song of Pi
x = int(raw_input())

p = "31415926535897932384626433833"
pi = list(p)
for i in range(x):
    s = raw_input()
    arr = s.split(" ")
    len = list()
    for j in range(arr.__len__()):
        len.append(arr[j].__len__())
    count = 0
    for k in range(len.__len__()):
        if (int(len[k]) == int(pi[k])):
            continue
        else:
            count += 1

    if count != 0:
        print "It's not a pi song."
    else:
        print "It's a pi song."
