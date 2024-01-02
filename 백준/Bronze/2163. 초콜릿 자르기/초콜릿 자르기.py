'''Solved date
- 230102
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

ans = (N-1) + (N * (M-1))

print(ans)
