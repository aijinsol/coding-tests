'''Solved date
- 230627
'''
import sys


input = sys.stdin.readline
A, B = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
a_b = a_set - b_set
b_a = b_set - a_set

print(len(a_b) + len(b_a))