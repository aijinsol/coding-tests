'''Date
- 240104
'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())

stack = []
for _ in range(N):
    command = input().rstrip()
    if command.startswith('push'):
        command, X = command.split()
        stack.append(int(X))
    elif command == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1) if not stack else print(0)
    elif command == 'top':
        print(stack[-1]) if stack else print(-1)
