'''Solved date
- 231121
'''
import sys


input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    money = int(input().rstrip())
    quarter, leftover = divmod(money, 25)
    dime, leftover = divmod(leftover, 10)
    nickel, penny = divmod(leftover, 5)
    print(quarter, dime, nickel, penny)
