'''Solved date
- 231219
'''
import sys

input = sys.stdin.readline
X = int(input().rstrip())
N = int(input().rstrip())

res = 0
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    res += a * b
    
if int(res) == X:
    print('Yes')
else:
    print('No')