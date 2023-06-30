'''Solved date
- 230630
'''
def solution(k, m, score):
    ans, i = 0, 0
    score.sort(reverse=True)
    for _ in range(len(score)//m):
        ans += min(score[i:i+m]) * m
        i += m
    return ans
