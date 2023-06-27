'''Solved date
- 230627
'''
import sys
from collections import defaultdict


input = sys.stdin.readline
N, M = map(int, input().split())

names = defaultdict(int)
for _ in range(N+M):
    names[input().rstrip()] += 1

def find_keys_by_value(dict, value):
    keys = []
    for key, val in dict.items():
        if val == value:
            keys.append(key)
    return keys

ans = sorted(find_keys_by_value(names, 2))

print(len(ans))

for a in ans:
    print(a)