'''Date
- 240124
'''
import sys


input = sys.stdin.readline

while True:
    nums = list(map(int, input().rstrip().split()))
    if nums[0] == nums[1] == 0:
        break
    elif nums[1] % nums[0] == 0:
        print("factor")
    elif nums[0] % nums[1] == 0:
        print("multiple")
    else:
        print("neither")