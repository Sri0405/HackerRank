# Modified Fibo
data = raw_input().rstrip().split(" ")
x = long(data[0])
y = long(data[1])
flag = 1
count = long(2);
while (flag == 1):
    z = long(pow(y, 2) + x)
    print z
    count = long(count) + 1
    temp = long(y)
    y = long(z)
    x = long(temp)
    if (long(z) == long(data[2])):
        flag = 0

print long(count)
