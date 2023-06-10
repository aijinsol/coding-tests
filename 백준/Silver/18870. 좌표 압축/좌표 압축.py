'''Solved date
- 230610
'''
import sys


input = sys.stdin.readline
_N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

sorted_numbers = sorted(numbers)
numbers_idx = dict()
idx = 0
for num in sorted_numbers:
    if num not in numbers_idx:
        numbers_idx[num] = idx
        idx += 1
    else:
        continue

for num in numbers:
    print(numbers_idx[num], end=' ')


# Bruce
import sys


input = sys.stdin.readline
N = int(input().rstrip())
X_list = list(map(int, input().rstrip().split()))
sorted_x_list = sorted(set(X_list))
val2idx = {val: idx for idx, val in enumerate(sorted_x_list)}
print(*map(val2idx.get, X_list))
