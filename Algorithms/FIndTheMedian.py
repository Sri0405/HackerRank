__author__ = 'sridhar'


def swap(x, y):
    temp = x
    x = y
    y = temp


def partition(arr, lo, hi):
    pivot = hi
    stored = lo
    for i in range(lo, hi):
        if (arr[i] < arr[pivot]):
            swap(arr[i], arr[stored])
            stored = stored + 1
    swap(arr[hi], stored)
    return lo


def select(arr,n):
    left =0
    right =arr.__len__()-1
    while(right>=left):
        pivotind = partition(arr,left,right)
        if(pivotind==n):
            return arr[pivotind]
        elif pivotind<n:
            left =pivotind+1
        elif pivotind>n:
            right = pivotind-1

for i in range(int(raw_input())):
    arr =map(int,raw_input().rstrip().split(" "))


select(arr,(arr.__len__()-1)/2 + 1)
