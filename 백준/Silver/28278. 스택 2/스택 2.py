'''Date
- 240106
'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())

stack = []
for _ in range(N):
    command = input().rstrip()
    if command.startswith('1'):
        stack.append(int(command.split()[-1]))
    elif command == '2':
        print(stack.pop()) if stack else print(-1)
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(0) if stack else print(1)
    elif command == '5':
        print(stack[-1]) if stack else print(-1)
