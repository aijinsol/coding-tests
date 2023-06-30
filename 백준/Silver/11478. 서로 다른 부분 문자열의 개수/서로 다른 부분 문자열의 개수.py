'''Solved date
- 230630
'''
import sys


input = sys.stdin.readline
str = input().rstrip()
ans = set()
for i in range(len(str)):
    for j in range(1, len(str)+1):
        ans.add(str[i:i+j])
        
print(len(ans))