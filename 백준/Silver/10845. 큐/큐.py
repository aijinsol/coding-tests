import sys
from collections import deque


sys_input = sys.stdin.readline


queue = deque()
N = int(sys_input().rstrip())
for _ in range(N):
    order = sys_input().rstrip()
    if order.startswith('push'):
        queue.append(int(order.split()[1]))
    elif order == 'pop':
        print(queue.popleft()) if queue else print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        print(0) if queue else print(1)
    elif order == 'front':
        print(queue[0]) if queue else print(-1)
    elif order == 'back':
        print(queue[-1]) if queue else print(-1)