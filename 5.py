"""Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import Counter

def factorize(n):
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factors.append(i)
                break
    return factors

def cumulative_biggest_factors(numbers):
    factor_counts = []
    for number in numbers:
        count = Counter(factorize(number))
        factor_counts += [count]
    final_count = {}
    for element in factor_counts:
        for item, count in element.items():
            if item not in final_count:
                final_count[item] = count
            elif final_count[item] < element[item]:
                final_count[item] = count
    result = 1
    for item, count in final_count.items():
        result = result * item ** count
    return result

print(cumulative_biggest_factors(range(1, 21)))