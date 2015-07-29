__author__ = 'sridhar'
# Cut Sticks Problem
n = int(raw_input())
nums = map(int,raw_input().rstrip().split(" "))
print nums.__len__()
for i in range(n):
    if nums.__len__()<=1:
        break
    min_in =min(nums)
    # print min_in
    nums=[num-min_in for num in nums]
    # print nums
    nums=[num for num in nums if num!=0]
    if nums.__len__()==0:
        break
    print nums.__len__()
