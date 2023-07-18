'''Solved date
- 230718
'''
import sys


input = sys.stdin.readline
ans = int(''.join(sorted(input(), reverse=True)))
print(ans)

'''
# Solution 2)
print(*sorted(input(), reverse=1), sep='')
'''
