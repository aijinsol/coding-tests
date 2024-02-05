'''Date
- 240205
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

def recur(N, M, sequence=[]):
    if len(sequence) == M:
        print(*sequence)
        return
    for num in range(1, N+1):
        if len(sequence) == 0 or num >= sequence[-1]:
            recur(N, M, sequence+[num])
            
recur(N, M)