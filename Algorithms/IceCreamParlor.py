__author__ = 'sridhar'

from itertools import combinations

for cases in range(int(raw_input())):
    M = int(raw_input())
    N = int(raw_input())

    arr = map(int, raw_input().rstrip().split(" "))

    combos = combinations(arr, 2)

    for pair in combos:
        if sum(pair) == M:
            indx1 = arr.index(pair[0])
            indx2 = arr.index(pair[1], indx1 + 1)
            print("{} {}".format(indx1 + 1, indx2 + 1))
            break
