'''Date
- 240124
'''
import sys


input = sys.stdin.readline
N, K = list(map(int, input().rstrip().split()))

res = []
for num in range(1, N+1):
    if N % num == 0:
        res.append(num)

print(res[K-1]) if len(res) >= K else print(0)