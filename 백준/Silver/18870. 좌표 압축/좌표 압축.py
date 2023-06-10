'''Solved date
- 230610
'''
import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

sorted_numbers = sorted(numbers)
numbers_idx = defaultdict(int)
idx = 0
for num in sorted_numbers:
    if num not in numbers_idx.keys():
        numbers_idx[num] = idx
        idx += 1
    else:
        continue

for num in numbers:
    print(numbers_idx[num], end=' ')