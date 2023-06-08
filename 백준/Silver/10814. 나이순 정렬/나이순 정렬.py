'''Solved
- 230608
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())
members = list()

for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))
members_sorted = sorted(members, key = lambda x : x[0], reverse=False)

for idx in range(N):
    print(members_sorted[idx][0], members_sorted[idx][1])