#! /usr/bin/env python
"""
Declares a differential calculator object class
which uses the central difference method to numerically approximate the derivative
of a function at a point. The numerically approximated derivative is then plotted
against the exact derivative for comparison.

Leon Hostetler, Mar. 30, 2017

USAGE: python differential_calculator.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np

class DiffCalc():
    """Differential calculator object class."""
    def __init__(self, func, h=1e-8):
        """Initialize"""
        self.f = func
        self.h = h

    def diff(self, x):
        """Derivative of f(x) approximated at x using the central difference method."""
        self.x = x
        return (self.f(self.x + self.h/2)/self.h) \
                - self.f(self.x - self.h/2)/self.h


def f(x):
    """
    Define f(x) = 1 + 0.5*tanh(2x).
    """
    return 1 + 0.5*np.tanh(2*x)


def dfdx(x):
    """
    The exact derivative of f(x)
    """
    return (np.cosh(2*x))**(-2)


res = 1000              # Plotting resolution
xlo, xhi = -2.0, 2.0    # Define the plotting region

# Construct the list of x-values
xlist = np.array([xlo + i*(xhi-xlo)/res for i in range(res+1)], float)

# Compute the lists of dfdx values and numerical derivative approximations
dfdxlist = dfdx(xlist)

# Compute the list of
der = DiffCalc(f)
difflist = der.diff(xlist)

# Plot the results
plt.rc('text', usetex=True)
plt.title("Exact Derivative vs. Numerical Approximation")
plt.plot(xlist, dfdxlist, label=r"$\frac{df}{dx}$")
plt.plot(xlist, difflist, label='Numerical Approximation', \
         linestyle="none", marker="x", markevery=20)
plt.legend(loc=1)
plt.xlabel(r"$x$")
plt.show()
