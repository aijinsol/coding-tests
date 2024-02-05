'''Date
- 240205
'''
import sys
from itertools import permutations


input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

numbers = list(range(1, N+1))
perms = list(permutations(numbers, M))

for perm in perms:
    print(*perm)