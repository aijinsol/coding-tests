'''Solved date
- 230714
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())

stars = list()
for idx in range(N):
    stars.append(' ' * (N-idx-1) + '*' * (2*idx+1) + ' ' * (N-idx-1))

stars.extend(stars[-2::-1])
for star in stars:
    print(star.rstrip())
