'''Solved date
- 230630
'''
def solution(name, yearning, photo):
    ans = []
    hash_map = dict()
    for n, y in zip(name, yearning):
        hash_map[n] = y
    for p in photo:
        score = 0
        for p_name in p:
            try:
                score += hash_map[p_name]
            except:
                continue
        ans.append(score)
    return ans


def solution(name, yearning, photo):
    hash_map = dict(zip(name, yearning))
    ans = []
    for p in photo:
        score = 0
        for p_name in p:
            if p_name in hash_map:
                score += hash_map[p_name]
        ans.append(score)
    return ans