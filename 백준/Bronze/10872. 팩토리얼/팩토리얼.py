'''Solved date
- 231217
'''

import sys

input = sys.stdin.readline

N = int(input().rstrip())

ans = 1
for n in range(1, N+1):
    ans *= n

print(ans)