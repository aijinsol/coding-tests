'''Solved date
- 231116
'''
import sys


# input = sys.stdin.readline
board = [[1] * 15 for _ in range(5)]

for row in range(5):
    letters = list(input().rstrip())
    for idx, letter in enumerate(letters):
        board[row][idx] = letter

new_board = list(map(list, zip(*board)))

result = ''
for letters in new_board:
    result += ''.join(str(item) for item in letters if isinstance(item, str))

print(result)