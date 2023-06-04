import sys
from collections import deque


input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque(range(1, N+1))
result = []

idx = 0
while len(queue):
    idx += 1
    if idx % K != 0:
        queue.rotate(-1)
    else:
        result.append(queue.popleft())
        
print('<' + str(result)[1:-1] + '>')