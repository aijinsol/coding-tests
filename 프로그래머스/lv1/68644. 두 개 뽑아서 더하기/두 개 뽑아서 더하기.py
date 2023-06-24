'''Solved date
- 230623
'''
def solution(numbers):
    ans = set()
    indexes = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                indexes.append((i,j))
                
    for idx in indexes:
        i, j = idx
        ans.add(numbers[i] + numbers[j])
    
    ans = sorted(list(ans))
    return ans


def solution(numbers):
    ans = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            ans.add(numbers[i] + numbers[j])
    return sorted(list(ans))


from itertools import combinations


def solution(numbers):
    ans = sorted(set(sum(i) for i in list(combinations(numbers, 2))))
    return ans