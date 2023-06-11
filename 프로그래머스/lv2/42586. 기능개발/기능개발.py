'''Solved date
- 230611
'''
from collections import deque


work_days = deque()
def solution(progresses, speeds):
    for idx, progress in enumerate(progresses):
        n = 1
        while progress + speeds[idx] * n < 100:
            n += 1
        work_days.append(n)
    print(work_days)
    
    idx = 1
    ans = []
    len_check = len(work_days)
    while work_days:
        pivot = work_days[0]
        print(f'{pivot=}')
        if len(work_days) == 1:
            ans.append(idx)
            break
        if pivot < work_days[idx]:
            ans.append(idx)
            print(f'{ans=}')
            for _ in range(idx):
                work_days.popleft()
            print(f'{work_days=}')
            print('==='*5)
            idx = 1
        else:
            idx += 1
            if sum(ans) + idx == len_check:
                ans.append(idx)
                break
    
    return ans