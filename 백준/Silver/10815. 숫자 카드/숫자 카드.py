'''Solved date
- 230624
'''
import sys

input = sys.stdin.readline
N = input()
cards = set(map(int, input().split()))
M = input()
check_nums = map(int, input().split())

for num in check_nums:
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
