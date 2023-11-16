'''Solved date
- 231116
'''
import sys


input = sys.stdin.readline
max_num = 0
row_idx, col_idx = 1, 1

for row in range(9):
    nums = list(map(int, input().split()))
    tmp = max(nums)
    if max_num < tmp:
        max_num = tmp
        row_idx, col_idx = row + 1, nums.index(max_num) + 1

print(max_num)
print(row_idx, col_idx)