'''Solved date
- 240123
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
        

def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
            
            
def solution(brown, yellow):
    area = brown + yellow
    for num in range(3, int(area ** 1/2) + 1):
        if (area % num == 0) and 2 * (area // num + num - 2) == brown:
            return [area // num, num]