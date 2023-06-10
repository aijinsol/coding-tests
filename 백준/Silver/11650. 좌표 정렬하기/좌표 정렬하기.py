'''Solved date
- 230608
'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())
coordinates = list()
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))
coordinates_sorted = sorted(coordinates, key = lambda x : (x[0], x[1]))

for idx in range(N):
    x, y = coordinates_sorted[idx]
    print(x, y)