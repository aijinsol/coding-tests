'''Solved date
- 231007
'''
import sys


input = sys.stdin.readline
T = int(input().rstrip())

def is_vps(ps: str) -> str:
    stack = []
    for p in ps:
        if not stack: # 비어있을 때
            stack.append(p)
        else: # 무언가 있을 때
            if stack[-1] == '(':
                if p == ')':
                    stack.pop()
                else:  # p == '('
                    stack.append(p) 
            else:  # stack[-1] == ')'
                stack.append(p)
    if stack:
        return 'NO'
    return 'YES'

for _ in range(T):
    ps = input().rstrip()
    print(is_vps(ps))