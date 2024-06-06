'''Solved date
- 240606
'''
def solution(start_num: int, end_num: int):
    ans = []
    for num in range(start_num, end_num-1, -1):
        ans.append(num)
    return ans