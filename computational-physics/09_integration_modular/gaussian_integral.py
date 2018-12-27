#! /usr/bin/env python
"""
Compute the value of the gaussian integral.
Since this integral is from negative infinity to infinity, we have to
perform a change of variables so the new limits of integration are [0,1].

Leon Hostetler, Mar. 7, 2017

USAGE: python gaussian_integral.py
"""

from __future__ import division, print_function
import mymodule_integration as mmi
import numpy as np


def f(x):
    """
    The Gaussian integral
        int_{-infty}^{infty} e^{-x^2} dx
    is over an infinite range, so we need to make a change of
    variables so that it is evaluated from 0 to 1. This function
    gives the integrand after that change of variables.
    """
    return (2/(1-x)**2)*np.exp(-(x/(1-x))**2)

epsilon = 1e-15  # To prevent divide by zero errors in integrand

trapz = mmi.integrate_trapz_adaptive(f, 0, 1-epsilon, 1e-10)
simps = mmi.integrate_simpson_adaptive(f, 0, 1-epsilon, 1e-10)
monte = mmi.integrate_monte_carlo(f, 0, 1, 100000)

actual = np.sqrt(np.pi)

print("\nThe actual value of the Gaussian integral is sqrt(pi) = ", actual, \
      ". Below, are the approximations using several different methods of " \
      "numerical integration along with the absolute error of each method.", sep="")

print("\nAdaptive Trapezoidal Method:", trapz[0])
print("Error: ", np.abs(actual - trapz[0]), sep="")

print("\nAdaptive Simpson's Rule:", simps[0])
print("Error: ", np.abs(actual - simps[0]), sep="")

print("\nMonte Carlo method (with N = 100,000):", monte)
print("Error: ", np.abs(actual - monte), sep="")
