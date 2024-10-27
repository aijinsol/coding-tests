def solution(a, b, n):
    # a: empty bottle per new bottle (마트로부터 새 병을 받기 위한 비어있는 병 단위)
    # b: new bottle 단위
    # n: 현재 내가 가지고 있는 병 수
    
    # new: 마트에서 새로 받는 병 수
    # leftover: 수중에 남아있는 병 수   
    ans = 0
    while n >= a:
        tmp, leftover = divmod(n, a)
        new = tmp * b
        ans += new
        n = leftover + new
    return ans