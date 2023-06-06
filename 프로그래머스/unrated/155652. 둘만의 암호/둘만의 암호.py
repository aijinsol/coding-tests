'''
solved date
- 230606
'''
from string import ascii_lowercase


def solution(s: str, skip: str, index: str) -> str:
    ans = ''
    alphabet_list = list(ascii_lowercase)
    for c in skip:
        alphabet_list.remove(c)
    for c in s:
        idx = (alphabet_list.index(c) + index) % len(alphabet_list)
        ans += alphabet_list[idx]
    return ans

def solution(s: str, skip: str, index: str) -> str:
    ans = ''
    alphabet_filtered = sorted(set(ascii_lowercase) - set(skip))
    for c in s:
        idx = (alphabet_filtered.index(c) + index) % len(alphabet_filtered)
        ans += alphabet_filtered[idx]
    return ans