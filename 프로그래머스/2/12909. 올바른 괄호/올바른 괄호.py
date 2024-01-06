'''Date
- 240106
'''
def solution(s):
    stack = []
    for p in s:
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()
        else:
            stack.append(p)
    ans = False if stack else True
    return ans