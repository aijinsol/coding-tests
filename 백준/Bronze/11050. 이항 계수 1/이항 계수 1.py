'''Solved date
- 231127
'''
import sys

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

def factorial(N):
    res = 1
    for n in range(1, N+1):
        res *= n
    return res

ans = int(factorial(N) / (factorial(N-K) * factorial(K)))
print(ans)
