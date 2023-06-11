'''Solved date
- 230611
'''
from collections import deque


def solution(progresses, speeds):
    # 1) Determine the number of days required for each task.
    work_days = deque()
    for idx, progress in enumerate(progresses):
        n = 1
        while progress + speeds[idx] * n < 100:
            n += 1
        work_days.append(n)
    
    # 2) Identify the number of tasks being deployed per date.
    idx = 1
    ans = []
    len_check = len(work_days)
    while work_days:
        pivot = work_days[0]
        if len(work_days) == 1:
            ans.append(1)
            break
        if pivot < work_days[idx]:
            ans.append(idx)
            for _ in range(idx):
                work_days.popleft()
            idx = 1
        else:
            idx += 1
            if sum(ans) + idx == len_check:
                ans.append(idx)
                break
    
    return ans

# Bruce
from collections import deque


def solution(progresses, speeds):
    ans = []
    queue = deque([[progress, speed] for progress, speed in zip(progresses, speeds)])
    while queue:

        cnt = 0
        for idx, (progress, speed) in enumerate(queue):
            queue[idx][0] += speed

        while queue and queue[0][0] >= 100:
            queue.popleft()
            cnt += 1

        if cnt:
            ans.append(cnt)
    return ans
