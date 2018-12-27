#! /usr/bin/env python
"""
Compute all the prime numbers up to 10,000 using an efficient algorithm.
Instead of checking if a number n is prime by dividing by all previous
numbers, or even all previous primes, this program only divides by
all previous primes less than or equal to the square root of n.

Leon Hostetler, Feb. 14, 2017

USAGE: python prime_numbers.py
"""
from __future__ import division, print_function

primes = [2]
print(2)

for n in range(3, 10001):
    i, k = 0, 0
    while primes[i] <= n**(1/2):    # No need to check against ALL smaller primes
        if n % primes[i] == 0:      # Check if divisible by previous primes
            k = 1
        i += 1
    if k == 0:                      # If good, at it to the list and print it
        primes.append(n)
        print(n)

# This produces a print-friendly (i.e. 2 pages) list of primes. Otherwise,
# you have to print 21 pages.
with open("primes.txt", "w") as text_file:
    for i in range(len(primes)):
        text_file.write(str(primes[i]) + ', ')
