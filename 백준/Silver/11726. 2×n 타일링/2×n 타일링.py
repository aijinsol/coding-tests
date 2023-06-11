import sys


def tile_cnt(num):
    dp = [1, 1]
    for i in range(2, num+1):
        dp.append(d[i-1] + d[i-2])
    return dp[num]

def tile_cnt(num):
    dp = [0] * (num+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, num+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[num]

input = sys.stdin.readline
n = int(input().strip())
print(tile_cnt(n) % 10007)
