'''Solved
- 230608
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())
members = list()

for _ in range(N):
    age, name = input().rstrip().split()
    members.append((int(age), name))
members_sorted = sorted(members, key = lambda x : x[0], reverse=False)

for age, name in members_sorted:
    print(age, name)
