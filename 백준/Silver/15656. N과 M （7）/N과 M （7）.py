'''Date
- 240206
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
numbers = sorted(map(int, input().rstrip().split()))

def recur(N, M, seq=[]):
    if len(seq) == M:
        print(*seq)
        return
    for num in numbers:
        recur(N, M, seq + [num])

recur(N, M)