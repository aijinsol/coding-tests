'''Solved date
- 230715
'''
import sys


input = sys.stdin.readline
n = int(input().rstrip())
papers = list()
for _ in range(n):
    papers.append(tuple(map(int, input().split())))
    
area = [[0] * 100 for _ in range(100)]

for x, y in papers:
    for pt_x in range(x, x+10):
        for pt_y in range(y, y+10):
            area[pt_x][pt_y] = 1

ans = str(area).count('1')
print(ans)