'''Solved date
- 230701
'''
def solution(food):
    res = ''
    for i, f in enumerate(food):
        res += str(i) * (f // 2)
    res = res + '0' + res[::-1]
    return res