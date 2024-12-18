def calculate_divisors_up_to(n):
    divisor_cnts = [0] * (n + 1)
    for i in range(1, n + 1):           # O(n)
        for j in range(i, n + 1, i):    # O(n/i)
            divisor_cnts[j] += 1
    return divisor_cnts

def solution(number, limit, power):
    divisor_cnts = calculate_divisors_up_to(number)
    
    for idx, div in enumerate(divisor_cnts):  # O(number)
        if div > limit:
            divisor_cnts[idx] = power
    
    ans = sum(divisor_cnts)             # O(number)
    return ans