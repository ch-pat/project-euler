"""Largest Palindromic Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome(number):
    number = str(number)
    for i in range(len(number)):
        if number[i] != number[len(number) - i - 1]:
            return False
        if i == len(number) - i - 1:
            return True
    return True

palindromes = []
for x in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(x*y):
            palindromes.append(x*y)

print(max(palindromes))