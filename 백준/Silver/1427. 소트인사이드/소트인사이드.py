'''Solved date
- 230718
'''
import sys


input = sys.stdin.readline
print(*sorted(input(), reverse=1), sep='')