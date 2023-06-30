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