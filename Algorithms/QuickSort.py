__author__ = 'sridhar'

def swap(A,x,y):
    # global count
    # count+=1
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
count =0
A = map(int, raw_input().rstrip().split(" "))
quicksort(A,0, len(A)-1)
print count