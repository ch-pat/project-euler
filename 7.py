"""10001ts Prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

def nth_prime(n):
    i = 0
    counter = 0
    while i < n:
        counter += 1
        if is_prime(counter):
            i += 1
    return counter

print(nth_prime(10001))
