"""Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

def factors(n):
    factors = {1}
    prime_candidates = (x for x in range(1, int(sqrt(n))) if is_prime(x))
    for i in prime_candidates:
        if n % i == 0:
            factors.add(i)
    return factors

print(factors(600851475143))

