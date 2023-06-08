'''Solved date
- 230608
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())
pts = list()
for _ in range(N):
    x, y = map(int, input().split())
    pts.append((x, y))
pts_sorted = sorted(pts, key = lambda x : (x[1], x[0]))

for idx in range(N):
    print(pts_sorted[idx][0], pts_sorted[idx][1])