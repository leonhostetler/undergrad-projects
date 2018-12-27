#! /usr/bin/env python
"""
Compute the probability that an unbiased coin
tossed n times, will come up heads exactly k times and k or more times.

Leon Hostetler, Jan. 31, 2017

USAGE: coin_probability.py
"""

from __future__ import division, print_function

# Main body of program

n = int(raw_input("Enter the number of tosses (n): "))
k = int(raw_input("Enter the number of heads (k): "))


def binomial(i, j):
    """
    This function computes the binomial n choose k using the formula
    (n(n-1)(n-1)...(n-k+1)) / (1*2*3*...*k)
    """
    if j == 0:
        return 1

    num, denom = 1, 1
    for m in range(i, i-j, -1):     # Compute the numerator
        num *= m
    for m in range(1, j+1):         # Compute the denominator
        denom *= m

    return int(num/denom)


def probability(i, j):
    """
    This function computes the probability that an unbiased coin
    tossed n times comes up heads exactly k times.
    """
    prob = binomial(i, j)/(2**i)
    return prob


def total_prob(i, j):
    """
    This function computes the probability that an unbiased coin
    tossed n times comes up heads k or more times.
    """
    total = 0
    for m in range(j, i+1):
        total += probability(i, m)
    return total


print("The probability that the coin comes up exactly ", k, " times is ", probability(n, k))
print("The probability that the coin comes up ", k, " or more times is ", total_prob(n, k))
