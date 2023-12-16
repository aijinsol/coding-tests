'''
Solved date
- 231216
'''
import sys
from collections import defaultdict


input = sys.stdin.readline
N = int(input())
n_cnt = defaultdict(int)

for _ in range(N):
    n_cnt[int(input())] += 1

for n in range(10000+1):
    for _ in range(n_cnt[n]):
        print(n)