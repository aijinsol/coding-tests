'''solved date
- 230606
'''
from collections import Counter


def solution(id_list, report, k):
    # 1) 같은 신고 로그 제거
    report = set(report)
    
    # 2) 유저별 신고 당한 횟수 세기 -> k번 이상 신고당한 이용 정지 유저 파악
    reported_list = [name.split()[1] for name in report]
    reported_counter = Counter(reported_list)
    blocked_usrs = []
    for id_, cnt in reported_counter.items():
        if cnt >= k:
            blocked_usrs.append(id_)
    
    # 3) 이용 정지 유저를 신고한 유저 파악
    reporters = dict.fromkeys(id_list, 0)
    for names in report:
        if names.split()[1] in blocked_usrs:
            reporters[names.split()[0]] += 1
    
    ans = [val for val in reporters.values()]
    return ans
    