from itertools import permutations


def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    candidates = set()
    for i in range(1, len(words) + 1):
        for p in permutations(words, i):
            candidates.add("".join(p))
            
    ans = 0
    for b in babbling:
        if b in candidates:
            ans +=1
    return ans
