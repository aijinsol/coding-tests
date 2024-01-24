'''Solved date
- 240123
- 240124
'''
def solution(brown, yellow):
    num_blocks = brown + yellow
    candidates = []
    for num in range(3, num_blocks):
        quotient, remainder = divmod(num_blocks, num)
        if num > quotient:
            break
        if remainder == 0:
            candidates.append([quotient, num])
            
    for candidate in candidates:
        row, col = candidate
        if (row-2) * (col-2) == yellow:
            return [row, col]

            
def solution(brown, yellow):
    area = brown + yellow
    for num in range(3, int(area ** 1/2) + 1): # num: 세로 길이
        # (넓이 % 세로 == 0) and 2 * (가로 + 세로) - 4 == 둘레
        if (area % num == 0) and 2 * (area // num + num)- 4 == brown:
            return [area // num, num]