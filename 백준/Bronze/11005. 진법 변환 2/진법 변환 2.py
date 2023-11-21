'''Solved date
- 231121
'''

import sys

input = sys.stdin.readline
N, B = map(int, input().rstrip().split())

num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

res = ''
while N:
    N, leftover = divmod(N, B)
    res += str(num_list[leftover])
    
res = res[::-1]

print(res)