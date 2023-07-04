'''Solved date
- 230703
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())

stack = []
for _ in range(N):
    order = input().split()
    if len(order) > 1:
        stack.append(order[1])
    elif order[0] == 'pop':
        print(stack.pop()) if len(stack) else print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    elif order[0] == 'top':
        print(stack[-1]) if len(stack) else print(-1)
