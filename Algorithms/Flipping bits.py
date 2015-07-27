# Flipping Bits
loop = int(raw_input())
sum = 0
for i in range(loop):

    num = int(raw_input())

    x = bin(num)[2:].zfill(32)
    s = list(x)

    for i in range(s.__len__()):
        if (s[i] == '1'):
            s[i] = '0'
        else:
            s[i] = '1'

    string = ''
    string = ''.join(map(str, s))
    print string
    sum = 0
    for i in range(string.__len__()):
        y = string.__len__()
        sum = sum + int(string[i]) * pow(2, y - i - 1)

    print sum
