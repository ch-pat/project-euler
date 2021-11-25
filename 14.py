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
import time

def collatz_sequence(n):
    sequence = []
    while n > 1:
        sequence.append(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
    sequence.append(1)
    return sequence


start = time.perf_counter()
limit = 1000000
sequences = {k:v for k, v in zip(range(1, limit + 1), [[]]*limit)}
counter = 0
skips = 0
for k, v in sequences.items():
    counter += 1
    if v:
        skips += 1
        continue
    else:
        if k % 2:
            new_sequence = collatz_sequence(k)
            while new_sequence:
                start_number = new_sequence.pop(0)
                if start_number <= limit and not sequences[start_number]:
                    sequences[start_number] = [start_number] + new_sequence
                else:
                    break
        else:
            step = k // 2
            if step <= limit and sequences[step]:
                sequences[k] = [k] + sequences[step]
            else:
                sequences[k] = collatz_sequence(k)
            previous_step = k * 2
            if previous_step <= limit and not sequences[previous_step]:
                current_step = k
                while previous_step <= limit:
                    sequences[previous_step] = [previous_step] + sequences[current_step]
                    previous_step = previous_step * 2
                    current_step = current_step * 2


longest = []
for n in range(1, 1000001):
    current = sequences[n]
    if len(current) > len(longest):
        longest = current
print(longest)
end = time.perf_counter() - start
print(end)
print(skips / counter)