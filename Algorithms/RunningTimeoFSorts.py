__author__ = 'sridhar'

def insertion_sort(l):
    global count_insertion
    for i in xrange(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j + 1] = l[j]
            j -= 1
            count_insertion += 1
        l[j + 1] = key

def swap(ar_temp,x,y):
    temp =ar_temp[x]
    ar_temp[x]=ar_temp[y]
    ar_temp[y]=temp

def partition(ar_temp, lo, hi):
    count_quick =0
    pivotIndex = hi
    pivotValue = ar_temp[pivotIndex]
    swap(ar_temp,pivotIndex,hi)
    storeIndex = lo
    for i in range(lo, hi):
        if ar_temp[i] < pivotValue:
            swap(ar_temp,i,storeIndex)
            count_quick+=1
            storeIndex = storeIndex + 1
    swap(ar_temp,storeIndex,hi)
    return storeIndex

def quicksort(ar_temp, lo, hi):
    if lo < hi:
        p=partition(ar_temp, lo, hi)
        # print ' '.join(map(str,A))
        quicksort(ar_temp, lo, p - 1)
        quicksort(ar_temp, p + 1, hi)


m = input()
ar =[int(i) for i in raw_input().strip().split()]
ar_temp =ar[:]
count_insertion = 0
count_quick=0
insertion_sort(ar)
quicksort(ar_temp,0, len(ar_temp)-1)

print count_quick
