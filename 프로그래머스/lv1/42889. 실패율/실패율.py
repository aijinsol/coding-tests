'''Solved date
- 230815
'''
from collections import defaultdict


def solution(N, stages):
    ans = []
    user_cur_stage = defaultdict(int)
    fail_rates = defaultdict(int)
    for stage in range(1, N+1+1):
        user_cur_stage[stage] = stages.count(stage)
    
    for stage in range(1, N+1):
        challengers = 0
        for key, val in user_cur_stage.items():
            if key >= stage:
                challengers += val
        if challengers != 0:
            fail_rates[stage] = user_cur_stage[stage] / challengers
        else:
            fail_rates[stage]
    
    fail_rates_sorted = sorted(fail_rates.items(), reverse=True, key=lambda x: x[1])
    for rates in fail_rates_sorted:
        ans.append(rates[0])

    return ans


def solution(N, stages):
    ans = []
    fail_rates = defaultdict(int)
    for stage in range(1, N+1):
        if stages:
            fail_rates[stage] = stages.count(stage) / len(stages)
            stages = [n for n in stages if n != stage]
        else:
            fail_rates[stage]
    fail_rates_sorted = sorted(fail_rates.items(), reverse=True, key=lambda x: x[1])
    for rates in fail_rates_sorted:
        ans.append(rates[0])
    return ans
