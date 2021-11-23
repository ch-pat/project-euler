"""Sum square difference
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n):
    return sum((x**2 for x in range(1, n + 1)))

def square_of_sum(n):
    return (n * (n + 1) // 2) ** 2

def sum_square_difference(n):
    return square_of_sum(n) - sum_of_squares(n)

print(sum_square_difference(100))