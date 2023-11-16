'''Solved date
- 231116
'''
import sys


input = sys.stdin.readline
board = [[1] * 15 for _ in range(5)]

for row in range(5):
    letters = list(input().rstrip())
    for idx, letter in enumerate(letters):
        board[row][idx] = letter

new_board = list(map(list, zip(*board)))

words = list()
for letters in new_board:
    word = ''
    for idx in range(5):
        if letters[idx] != 1:
            word += letters[idx]
    words.append(word)

ans = ''.join(words)

print(ans)
