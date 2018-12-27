#! /usr/bin/env python
"""
Simulate rolling a pair of dice 1,000,000 times and estimates
the probability of getting a double six.

Leon Hostetler, Mar. 7, 2017

USAGE: python rolling_dice.py
"""

from __future__ import division, print_function
import random as rnd

# Simulate rolling a pair of dice
print("\nYour pair of dice yielded:", rnd.randint(1, 6), rnd.randint(1, 6))

# Roll a million pairs
sixes = 0
for i in range(1000000):
    if rnd.randint(1, 6) == 6 and rnd.randint(1, 6) == 6:
        sixes += 1

print("\nFor a million throws, the fraction of double sixes was: ", sixes/1000000, sep="")
