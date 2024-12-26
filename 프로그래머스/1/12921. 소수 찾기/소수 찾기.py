import math


def solution(n):
    primes = []
    for candidate in range(2, n + 1):
        is_prime = True
        for divider in range(2, int(math.sqrt(candidate)) + 1):
            if candidate % divider == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return len(primes)