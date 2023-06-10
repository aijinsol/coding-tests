'''Solved date
- 230608
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())
pts = list()
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    pts.append((x, y))
pts_sorted = sorted(pts, key = lambda x : (x[1], x[0]))

for x, y in pts_sorted:
    print(x, y)
