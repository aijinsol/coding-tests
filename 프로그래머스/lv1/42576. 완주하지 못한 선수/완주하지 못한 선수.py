'''Solved date
- 230617
'''
def solution(participant, completion):
    p_acc, c_acc = 0, 0
    hashmap = dict()
    for p in participant:
        p_hash = hash(p)
        hashmap[p_hash] = p
        p_acc += p_hash
    for c in completion:
        c_hash = hash(c)
        c_acc += c_hash
        
    ans = hashmap[p_acc - c_acc]
    return ans


def solution(participant, completion):
    acc = 0
    hashmap = dict()
    for p in participant:
        hash_val = hash(p)
        hashmap[hash_val] = p
        acc += hash_val
    for c in completion:
        acc -= hash(c)
        
    ans = hashmap[acc]
    return ans


from collections import Counter


def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    ans = list(p - c)[0]
    return ans
