'''Solved date
- 231007
'''
import sys

# input = sys.stdin.readline
T = int(input().rstrip())


def is_vps(ps: str) -> None:
    stack = []
    for p in ps:
        if stack: # 무언가 있을 때
            if stack[-1] == '(' and p == ')':
                stack.pop()
            else:
                stack.append(p)
        else: # 비어있을 때
            stack.append(p)
            
    print('NO') if stack else print('YES')

for _ in range(T):
    ps = input().rstrip()
    is_vps(ps)
    
    
# Bruce
'''
import sys


def chk_vps(ps: str):
    stack = []
    for c in ps:
        if stack and stack[-1] == "(" and c == ")":
            stack.pop()
        else:
            stack.append(c)
    print("YES") if not stack else print("NO")


input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    ps = input().rstrip()
    chk_vps(ps)
'''
