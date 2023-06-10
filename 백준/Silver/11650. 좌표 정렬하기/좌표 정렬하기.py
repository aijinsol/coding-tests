'''Solved date
- 230608
'''
import sys

input = sys.stdin.readline
N = int(input().rstrip())
coordinates = list()
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    coordinates.append((x, y))
coordinates_sorted = sorted(coordinates, key = lambda x : (x[0], x[1]))

for x, y in coordinates_sorted:
    print(x, y)
