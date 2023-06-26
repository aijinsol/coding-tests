'''Solved date
- 230626
'''
import sys


input = sys.stdin.readline
n = int(input().rstrip())

employers = dict()
ans = list()
for _ in range(n):
    name, log = input().rstrip().split()
    employers[name] = log
for name, log in employers.items():
    if log == 'enter':
        ans.append(name)

ans.sort(reverse=True)
for name in ans:
    print(name)