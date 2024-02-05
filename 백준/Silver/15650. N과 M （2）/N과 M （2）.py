'''Date
- 240205
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

def generate_sequences(N, M, sequence=[]):
    if len(sequence) == M:
        print(*sequence)
        return
    for num in range(1, N+1):
        if len(sequence) == 0 or num > sequence[-1]:
            generate_sequences(N, M, sequence+[num])
            
generate_sequences(N, M)