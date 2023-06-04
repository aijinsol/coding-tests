'''Solved date
- 230505
'''

def solution(t: str, p: str) -> int:
    nums_list = []
    idx, end_idx = 0, len(p)
    while end_idx <= len(t):
        nums_list.append(t[idx:end_idx])
        idx += 1
        end_idx += 1

    ans = 0
    for num in nums_list:
        ans += 1 if int(num) <= int(p) else 0
    return ans



def solution(t, p):
    ans = 0
    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            ans += 1
    return ans