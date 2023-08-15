'''Solved date
- 230815
'''
def solution(board, moves):
    dolls = []
    res = 0
    for move in moves:
        for idx, floor in enumerate(board):
            item = floor[move-1]
            if item != 0:
                if dolls and dolls[-1] == item:
                    dolls.pop()
                    res += 2
                else:
                    dolls.append(item)
                board[idx][move-1] = 0
                break
    return res


# Bruce
from typing import List


def solution(board: List[List[int]], moves: List[int]) -> int:
    N = len(board)
    ans = 0
    basket = []
    for m in moves:
        for idx in range(N):
            n = board[idx][m-1]
            if n != 0:
                board[idx][m-1] = 0
                if basket and basket[-1] == n:
                    basket.pop()
                    ans += 2
                else:
                    basket.append(n)
                break
    return ans
