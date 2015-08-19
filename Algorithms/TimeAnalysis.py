__author__ = 'sridhar'

def insertion_sort(l):
    global count
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           count +=1
        l[j+1] = key

def swap(A,x,y):
    global count_n
    count_n+=1
    temp =A[x]
    A[x]=A[y]
    A[y]=temp

def partition(A, lo, hi):
    pivotIndex = hi
    pivotValue = A[pivotIndex]
    swap(A,pivotIndex,hi)
    storeIndex = lo
    for i in range(lo, hi):
        if A[i] < pivotValue:
            swap(A,i,storeIndex)
            storeIndex = storeIndex + 1
    swap(A,storeIndex,hi)
    return storeIndex

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        print ' '.join(map(str,A))
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

x = raw_input()
count_n =0
count =0
A = ar = map(int, raw_input().rstrip().split(" "))
quicksort(A,0, len(A)-1)
insertion_sort(ar)

print count_n,count