"""Largest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def calculate_whole_sequences():
    import time
    memo = {1 : [1]}

    def collatz_sequence(n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            sequence = [n] + collatz_sequence(n * 3 + 1, memo)
            memo[n] = sequence
            return sequence 
        else:
            sequence = [n] + collatz_sequence(n // 2, memo)
            memo[n] = sequence
            return sequence


    start = time.perf_counter()
    limit = 1000000

    for i in range(1, limit + 1):
        collatz_sequence(i, memo)

    longest = []
    for n in range(1, 1000001):
        current = memo[n]
        if len(current) > len(longest):
            longest = current
    print(longest)

    end = time.perf_counter() - start
    print(end)


def lengths_only():
    import time
    memo = {1 : 1}

    def collatz_sequence(n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            sequence = 1 + collatz_sequence(n * 3 + 1, memo)
            memo[n] = sequence
            return sequence 
        else:
            sequence = 1 + collatz_sequence(n // 2, memo)
            memo[n] = sequence
            return sequence


    start = time.perf_counter()
    limit = 1000000

    for i in range(1, limit + 1):
        collatz_sequence(i, memo)

    longest = 0
    cur_idx = 0
    for n in range(1, 1000001):
        current = memo[n]
        if current > longest:
            longest = current
            cur_idx = n
    print(cur_idx, memo[cur_idx])

    end = time.perf_counter() - start
    print(end)

if __name__ == "__main__":
    lengths_only()