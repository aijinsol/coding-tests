'''Solved date
- 231117
'''
import sys


input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

matrix_a = [list(map(int, input().rstrip().split())) for _ in range(N)]
matrix_b = [list(map(int, input().rstrip().split())) for _ in range(N)]
    
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        matrix_a[i][j] += matrix_b[i][j]
        
for row in matrix_a:
    print(*row)