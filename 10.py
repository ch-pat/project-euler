"""Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt

def is_prime(n):
    if n in (0, 1):
        return False
    factors = {1, n}
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0 and i not in factors:
            return False
    return True

def prime_sum(n):
    candidates = [x for x in range(3, n + 1, 2)]
    total = 0
    primes = [2]
    while candidates:
        current = candidates[0]
        primes.append(current)
        candidates = [x for x in candidates if x % current]
        if current > sqrt(n) + 1:
            primes += candidates
            break
    return sum(primes)

print(prime_sum(2000000))