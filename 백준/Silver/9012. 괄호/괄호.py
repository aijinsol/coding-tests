'''Date
- 230704
- 231007
- 240106
'''
import sys


input = sys.stdin.readline
T = int(input().rstrip())

def is_vps(ps: str) -> str:
    stack = []
    for p in ps:
        if not stack: # 비어있을 때
            stack.append(p)
            if stack[0] == ')':
                return 'NO'
        elif stack[-1] == '(': # 비어있지않고, 마지막 원소 '('일 때
            if p == ')':
                stack.pop()
            else:  # p == '('
                stack.append(p) 
    if stack:
        return 'NO'
    return 'YES'

for _ in range(T):
    ps = input().rstrip()
    print(is_vps(ps))