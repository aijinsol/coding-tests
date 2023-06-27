'''Solved date
- 230627
'''
import sys
from collections import defaultdict


input = sys.stdin.readline

N = int(input().rstrip())
cards = map(int, input().split())
cards_cnt = defaultdict(int)
for card in cards:
    cards_cnt[card] += 1

M = int(input().rstrip())
check_nums = map(int, input().split())
for num in check_nums:
    print(cards_cnt[num], end = ' ')