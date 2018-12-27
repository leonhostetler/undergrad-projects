#! /usr/bin/env python
"""
Integrate a given function using the adaptive
trapezoidal method as well as the adaptive Simpson's method. In both cases,
the methods are imported from an external user-created module named
mymodule_integration.

Leon Hostetler, Mar. 7, 2017

USAGE: python adaptive_integration.py
"""

from __future__ import division, print_function
from mymodule_integration import integrate_trapz_adaptive, integrate_simpson_adaptive
import numpy as np


def f(x):
    """
    Returns the integrand evaluated at x.
    """
    return np.sin(np.sqrt(100*x))**2

print("\nAdaptive Trapezoidal Method:")
integrate_trapz_adaptive(f, 0, 1, 1e-6, True)

print("\nAdaptive Simpson's Rule:")
integrate_simpson_adaptive(f, 0, 1, 1e-6, True)
