#! /usr/bin/env python
"""
Plots a given polynomial so you can approximately
locate the roots. Then after you have seen the graph, it asks you how
many roots you want to find and where to look for them. Each root is
located using Newton's method.

Leon Hostetler, Mar. 21, 2017

USAGE: python polynomial_root.py
"""

from __future__ import division, print_function
import mymodule_root_finding as mmr
import matplotlib.pyplot as plt
import numpy as np

#
# Define the polynomial and its derivative
#

def P(x):
    """
    The polynomial we want to find the roots of.
    """
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1


def dPdx(x):
    """
    The first derivative of the polynomial.
    """
    return 5544*x**5 - 13860*x**4 + 12600*x**3 - 5040*x**2 + 840*x - 42

#
# Graph the polynomial to approximately locate the roots
#

x = np.linspace(0, 1, 1000)
y = P(x)

plt.plot(x, y)
plt.plot(x, np.zeros((len(x))))
plt.title("P(x)")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.show()

#
# Find the roots
#

prec = float(raw_input("\nWhat precision do you want? Enter a number: "))
roots = int(raw_input("How many roots do you want to find? Enter a number: "))

for i in range(roots):
    string = "\nWhat is your guess for root " + str(i+1) + "? Enter a real number: "
    guess = float(raw_input(string))
    root = mmr.newton(P, dPdx, guess, prec)[0]
    print("A root near your guess value is: x = ", root, sep="")
