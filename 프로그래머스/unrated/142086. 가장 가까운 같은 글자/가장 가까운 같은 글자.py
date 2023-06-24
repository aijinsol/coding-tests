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

# Bruce
def solution(s):
    ans = []
    hashmap = dict()
    for idx, c in enumerate(s):
        if c not in hashmap:
            ans.append(-1)
        else:
            ans.append(idx - hashmap[c])
        hashmap[c] = idx
    return ans
