# Find the Lonely Integer in given set
import collections


def lonelyinteger(a):
    counts = collections.defaultdict(int)
    for num in a:
        counts[num] += 1
    print counts
    for num, count in counts.items():
        if count % 2 == 1:
            return num


if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
