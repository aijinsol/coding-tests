'''Solved date
- 240123
'''
def solution(brown, yellow):
    num_blocks = brown + yellow
    candidates = []
    for num in range(3, num_blocks//2):
        quotient, remainder = divmod(num_blocks, num)
        if remainder == 0:
            candidates.append([quotient, num])
    
    for candidate in candidates:
        row, col = candidate
        if (row-2) * (col-2) == yellow:
            return [row, col]