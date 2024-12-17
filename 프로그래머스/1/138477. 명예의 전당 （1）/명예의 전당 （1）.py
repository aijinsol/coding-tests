def solution(k, score):
    ans = []
    winners = []
    for s in score:
        winners.append(s)
        new_winners = sorted(winners)[-k:]
        ans.append(new_winners[0])
    return ans