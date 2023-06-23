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