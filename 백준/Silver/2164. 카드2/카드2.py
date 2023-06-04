import sys
from collections import deque


input = sys.stdin.readline
n = int(input().rstrip())
queue = deque(range(n, 0, -1))

while len(queue) > 1:
    queue.pop()
    queue.rotate()

print(queue[0])