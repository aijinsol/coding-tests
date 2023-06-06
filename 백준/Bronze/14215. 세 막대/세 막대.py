'''solved date
- 230606
'''
# 삼각형 성립 조건: '가장 긴 변의 길이' < '다른 두 변의 길이의 합'
import sys


input = sys.stdin.readline
x, y, z = map(int, input().split())
sorted_l = sorted([x, y, z])
if sorted_l[-1] < sum(sorted_l[:2]):
    ans = sum(sorted_l)
else:
    ans = (sum(sorted_l[:2]) - 1) * 2 + 1

print(ans)