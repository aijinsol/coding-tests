'''Solved date
- 230704
'''
import sys


input = sys.stdin.readline
K = int(input().rstrip())

res = []
for _ in range(K):
    num = int(input().rstrip())
    res.append(num) if num != 0 else res.pop()

print(sum(res))