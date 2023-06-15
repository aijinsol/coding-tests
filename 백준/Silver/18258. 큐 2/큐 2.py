import sys
from collections import deque


input = sys.stdin.readline
N = int(input().rstrip())
queue = deque()

for _ in range(N):
    order = str(input().rstrip())
    if order.startswith('push'):
        queue.appendleft(int(order.split()[1]))
    elif order == 'pop':
        print(queue.pop()) if queue else print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(1) if not queue else print(0)
    elif order == 'front':
        print(queue[-1]) if queue else print(-1)
    elif order == 'back':
        print(queue[0]) if queue else print(-1)
