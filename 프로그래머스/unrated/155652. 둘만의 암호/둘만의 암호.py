'''
solved date
- 230606
'''

def solution(s, skip, index):
    ans = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = [c for c in alphabet]
    for c in skip:
        alphabet_list.remove(c)
    for c in s:
        new_idx = alphabet_list.index(c) + index
        if new_idx >= len(alphabet_list):
            new_idx %= len(alphabet_list)
        ans += alphabet_list[new_idx]
    return ans