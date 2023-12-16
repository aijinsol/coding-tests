'''Solved date
- 231216
'''
import sys


input = sys.stdin.readline

N, k = map(int, input().rstrip().split())
scores = list(map(int, input().rstrip().split()))

scores.sort(reverse=True)
print(scores[k-1])