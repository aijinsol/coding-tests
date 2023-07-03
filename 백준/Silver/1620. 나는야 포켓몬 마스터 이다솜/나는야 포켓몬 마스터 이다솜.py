'''Solved date
- 230703
'''
import sys


input = sys.stdin.readline
N, M = map(int, input().split())
hashmap = dict()
idx = 1

for _ in range(N):
    hashmap[idx] = input().rstrip()
    idx += 1

hashmap_converted = {val : key for key, val in hashmap.items()}

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(hashmap[int(question)])
    else:
        print(hashmap_converted[question])


# Bruce
import sys


input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
hashmap = dict()
for n in range(1, N+1):
    pokemon = input().rstrip()
    hashmap[n] = pokemon
    hashmap[pokemon] = n
    
for m in range(M):
    question = input().rstrip()
    if question.isdigit():
        question = int(question)
    print(hashmap[question])
