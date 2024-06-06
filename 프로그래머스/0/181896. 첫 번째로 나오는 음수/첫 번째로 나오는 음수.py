'''Solved date
- 240606
'''
from typing import List


def solution(num_list: List[int]):
    for idx, num in enumerate(num_list):
        if num < 0:
            return idx
    return -1
