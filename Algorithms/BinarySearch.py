__author__ = 'sridhar'


def BinarySearch(arr, key, left=0, right=None):
    if right == None: right = arr.__len__()
    if left > right:
        return False
    else:
        mid = left + (right - left) / 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return BinarySearch(arr, key, left, mid - 1)
        else:
            return BinarySearch(arr, key, mid + 1, right)




ara = [4,5,3,2]
print BinarySearch(ara,3)


