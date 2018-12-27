#! /usr/bin/env python
"""
Solve a quadratic equation in three different ways. The
first method uses the familiar form of the quadratic formula, and the second form
uses a rearranged form of the quadratic formula. Both of them suffer from numerical
error when b^2 >> 4ac. The third method eliminates these numerical errors.

Leon Hostetler, Feb. 21, 2017

USAGE: python quadratic_equations.py
"""

from __future__ import division, print_function
import numpy as np

# Input

s = raw_input("Enter three space-separated numbers a, b, and c \
defining a quadratic equation of the standard form: ")

myNums = [float(i) for i in s.split()]
a = myNums[0]
b = myNums[1]
c = myNums[2]

# Input verification

while b**2 - 4*a*c < 0.0:
    print("ERROR: The quadratic equation you entered has complex roots.",
          "This program is not designed to handle those.",
          "Please enter coefficients for a quadratic with real roots.")
    s = raw_input("Enter three space-separated numbers a, b, and c \
    defining a quadratic equation of the standard form: ")

    myNums = [float(i) for i in s.split()]
    a = myNums[0]
    b = myNums[1]
    c = myNums[2]

# Functions

def quadratic_formula_original(a, b, c):
    """
    This function computes the solutions to a quadratic equation using
    the regular form of the quadratic formula that everyone knows.
    """
    x1 = (-b + np.sqrt(b*b - 4*a*c))/(2*a)
    x2 = (-b - np.sqrt(b*b - 4*a*c))/(2*a)
    return x1, x2


def quadratic_formula_modified(a, b, c):
    """
    This function computes the solutions to a quadratic equation using
    a modified form of the quadratic formula.
    """
    x1 = (-2*c)/(b + np.sqrt(b*b - 4*a*c))
    x2 = (-2*c)/(b - np.sqrt(b*b - 4*a*c))
    return x1, x2


def quadratic_formula_final(a, b, c):
    """
    This function computes the solutions to a quadratic equation using
    a modified form of the familiar quadratic formula. It is modified
    such that the subtraction of large, nearly equal numbers (which causes
    numerical error) does not occur.
    """
    if b >= 0.0:
        x1 = (-2*c)/(b + np.sqrt(b*b - 4*a*c))
        x2 = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
    else:
        x1 = (-b + np.sqrt(b*b - 4*a*c))/(2*a)
        x2 = (-2*c)/(b - np.sqrt(b*b - 4*a*c))

    return x1, x2

# Results

print("\nThe original form of the quadratic formula gives the following solutions:")
print(quadratic_formula_original(a, b, c))

print("\nThe modified form of the quadratic formula gives the following solutions:")
print(quadratic_formula_modified(a, b, c))

print("\nThe optimal form of the quadratic formula, which reduces the numerical",
      "errors caused by the subtraction of large, nearly equal numbers gives",
      "the following solutions:")
print(quadratic_formula_final(a, b, c))
