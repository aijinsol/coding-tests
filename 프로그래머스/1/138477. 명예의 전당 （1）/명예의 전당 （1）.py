def solution(k, score):
    ans = []
    winners = []
    for s in score:
        winners.append(s)
        if (len(winners) > k):
            winners.remove(min(winners))
        ans.append(min(winners))
    return ans