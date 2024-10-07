def solution(num_list):
    sum_odd, sum_even = 0, 0
    for idx, num in enumerate(num_list, start=1):
        if idx % 2 != 0:
            sum_odd += num
        else:
            sum_even += num
    
    ans = max(sum_odd, sum_even) if sum_odd != sum_even else sum_odd
    
    return ans