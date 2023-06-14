'''Solved date
- 230614
'''
import sys


def solution(N, scores):
    max_score = max(scores)
    new_scores = map(lambda x: x / max_score * 100, scores)
    ans = float(sum(new_scores) / N)
    return ans

input = sys.stdin.readline
N = int(input().rstrip())
scores = list(map(int, input().split()))
print(solution(N, scores))
