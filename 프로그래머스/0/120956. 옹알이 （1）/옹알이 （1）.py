def solution(babbling):
    ans = 0
    for babble in babbling:
        for pivot in ["aya", "ye", "woo", "ma"]:
            babble = babble.replace(pivot, ' ')
        ans += 1 if not babble.strip() else 0
    return ans
