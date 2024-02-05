'''Date
- 240205
'''
import sys
from itertools import permutations


input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
numbers = map(int, input().rstrip().split())

perms = sorted(list(permutations(numbers, M)))
for perm in perms:
    print(*perm)