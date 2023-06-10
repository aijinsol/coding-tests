'''Soved date
- 230610
'''
import sys


input = sys.stdin.readline
N = int(input().rstrip())
words = set()

for _ in range(N):
    words.add(input().rstrip())

words_sorted = sorted(words, key = lambda x : (len(x), x))

for word in words_sorted:
    print(word)