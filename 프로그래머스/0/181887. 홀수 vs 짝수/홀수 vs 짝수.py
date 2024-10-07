def solution(num_list):
    sum_odd = sum(num_list[::2])
    sum_even = sum(num_list[1::2])
    return max(sum_odd, sum_even)