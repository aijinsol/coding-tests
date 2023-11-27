'''Solved date
- 231127
'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())

ans = N * (N-1)

print(ans)