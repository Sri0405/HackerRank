# Angry Professor - check the number of students Problem
x = int(raw_input())
for i in range(x):
    data = (raw_input().rstrip().split())
    stud = (raw_input().rstrip().split())
    count = 0
    for i in range(int(data[0])):
        if int(stud[i]) <= 0:
            count = count + 1
    if (count >= int(data[1])):
        print "NO"
    else:
        print "YES"
