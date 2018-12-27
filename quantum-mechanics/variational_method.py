#! /usr/bin/env python
"""
Uses the variational method to approximate the ground state energy
of the infinite square well.

Leon Hostetler, Feb. 27, 2017

USAGE: python variational_method.py

"""
from __future__ import division, print_function
import numpy as np
from scipy.integrate import quad
from sympy import *

L = 1
x = symbols('x')

def psi_squared(a):
    # This function allows us to evaluate our integrand at a point x = a
    return psi2.evalf(subs={x: a})


def k(a):
    # This function allows us to evaluate our integrand at a point x = a
    return integrand.evalf(subs={x: a})


# Estimate the ground state wave function by minimizing the function
# (x(L-x))^p with respect to varying p

# Estimate with a range of values for the exponent and print the estimate
# The best estimate is the smallest one
for i in np.linspace(0.5, 10, 100):
    psi = (x ** i) * (L - x) ** i
    psi2 = psi * psi
    g = diff(psi, x, x)
    integrand = -(0.5)*psi * g
    norm1, err1 = quad(psi_squared, 0, L)
    normConstant = 1 / norm1
    ans, err = quad(k, 0, L)
    E0 = normConstant * ans
    print("i = ", i, "E0 = ", E0)


print("The smallest E0 is the best estimate for the given range.")

# The exact answer for the ground state energy is pi^2/2 ~ 4.9348
