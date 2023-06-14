'''Solved date
- 230614
'''
import sys


def solution(num):
    sum, row = 0, 0
    
    # 1) Find the row number
    while sum < num:
        row += 1
        sum += row
    
    # 2) Find the column number
    col = int(num - (row - 1) * row / 2)
    
    # 3) Even rows: increasing numerator; Odd row: decreasing numerator
    if row % 2 == 0:
        ans = str(col) + '/' + str(row + 1 - col)
    else:
        ans = str(row + 1 - col) + '/' + str(col)
    
    return ans

input = sys.stdin.readline
num = int(input().rstrip())
print(solution(num))
