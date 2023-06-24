'''Solved date
- 230624
'''
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
S = set()
check_words = list()

for _ in range(N):
    S.add(input().rstrip())
for _ in range(M):
    check_words.append(input().rstrip())
    
ans = 0
for word in check_words:
    if word in S:
        ans += 1

print(ans)


# Solution 2)
import sys


N, M = map(int, sys.stdin.readline().strip().split())
str = sys.stdin.read().split()
S, command = set(str[:N]), str[N:]
print(sum(1 for i in command if i in S))
