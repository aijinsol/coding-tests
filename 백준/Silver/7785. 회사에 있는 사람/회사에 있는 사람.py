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

'''
# Bruce    
import sys


input = sys.stdin.readline
n = int(input().rstrip())

working = set()
for _ in range(n):
    name, log = input().rstrip().split()
    if log == "enter":
        working.add(name)
    else:
        working.remove(name)
        
ans = sorted(working, reverse=True)
for a in ans:
    print(a)
'''