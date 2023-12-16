'''Solved date
- 231216
'''
import sys


input = sys.stdin.readline

nums = list()
for _ in range(5):
    nums.append(int(input().rstrip()))

nums.sort()
 
print(int(sum(nums)/5))
print(nums[2])