'''Solved date
- 230714
'''
import sys


input = sys.stdin.readline

word = input().rstrip()
print(1) if word == word[::-1] else print(0)