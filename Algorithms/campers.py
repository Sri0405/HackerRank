__author__ = 'sridhar'

N, K = map(int, raw_input().rstrip().split(" "))
indx = map(int, raw_input().rstrip().split(" "))

list_f_taken = []
count=0

for i in indx:
    list_f_taken.append(i)

length = list_f_taken.__len__()

for i in range(1,N+1):
    if (i==1):
        if(i + 1 not in list_f_taken and i not in list_f_taken):
            list_f_taken.append(i)
            count+=1
    elif (i==N):
        if(i - 1 not in list_f_taken and i not in list_f_taken):
            list_f_taken.append(i)
            count+=1
    elif (i + 1 not in list_f_taken and i - 1 not in list_f_taken and i not in list_f_taken):
           list_f_taken.append(i)
           count+=1

print count+length