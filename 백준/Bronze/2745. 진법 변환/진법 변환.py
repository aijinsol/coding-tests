'''Solved date
- 231121
'''

import sys


input = sys.stdin.readline
N, B = input().split()

num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = N[::-1]
B = int(B)

res = 0
for idx, num in enumerate(N):
    res += num_list.index(num) * (B ** idx)
    
print(res)
