# Check String Funny
num_of = int(raw_input())

for i in range(num_of):
    str = raw_input()
    str_rev= str[::-1]
    count =0
    for j in range(1,str.__len__()):
        if abs(ord(str[j])-ord(str[j-1]))==abs(ord(str_rev[j])-ord(str_rev[j-1])):
           continue
        else:
            count+=1
    if count!=0:
        print "Not Funny"
    else:
        print "Funny"