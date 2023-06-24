'''Solved date
- 230624
'''
def solution(s):
    ans = []
    for i, c in enumerate(s):
        if s[:i].find(c) == -1:
            ans.append(-1)
        else:
            idx = abs(s[:i][::-1].find(c)) + 1
            ans.append(idx)
    return ans
