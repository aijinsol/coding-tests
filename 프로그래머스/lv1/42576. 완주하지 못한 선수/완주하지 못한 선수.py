'''Solved date
- 230614
'''
# def solution(participant, completion):
#     for p in participant:
#         if p in completion:
#             completion.remove(p)
#         else:
#             return p

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
