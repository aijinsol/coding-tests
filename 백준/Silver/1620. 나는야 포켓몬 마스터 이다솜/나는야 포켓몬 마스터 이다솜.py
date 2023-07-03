'''Solved date
- 230703
'''
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
hashmap = dict()
idx = 1

for _ in range(N):
    hashmap[idx] = input().rstrip()
    idx += 1

hashmap_converted = {val : key for key, val in hashmap.items()}

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(hashmap[int(question)])
    else:
        print(hashmap_converted[question])