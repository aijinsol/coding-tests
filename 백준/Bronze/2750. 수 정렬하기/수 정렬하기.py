'''Solved date
- 231125
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())

num_list = sorted([int(input().rstrip()) for _ in range(N)])

for num in num_list:
    print(num)