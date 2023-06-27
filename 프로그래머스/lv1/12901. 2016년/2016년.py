'''Solved date
- 230627
'''
def solution(a, b):
    months = {1: 31,
            2: 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31}
    days = 0
    for month in range(1, a):
        days += months[month]
    days += b
    if days % 7 == 0:
        ans = 'THU'
    elif days % 7 == 1:
        ans = 'FRI'
    elif days % 7 == 2:
        ans = 'SAT'
    elif days % 7 == 3:
        ans = 'SUN'
    elif days % 7 == 4:
        ans = 'MON'
    elif days % 7 == 5:
        ans = 'TUE'
    else:
        ans = 'WED'
    return ans
