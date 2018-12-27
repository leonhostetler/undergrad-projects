#! /usr/bin/env python
"""
Numerically approximate the gaussian error function
    E(x) = integrate( exp(-t^2), t, 0, x )
by using trapezoidal integration. E(x) is evaluated for many values of
x and plotted to obtain a plot of the Gaussian error function.

Leon Hostetler, Feb. 25, 2017

USAGE: python gaussian_errfn.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt


def f(t):
    """
    This defines the integrand of the Gaussian error function E(x).
    """
    return np.exp(-t**2)


def E(x, N):
    """
    This function computes the Gaussian error function
        E(x) = integrate( exp(-t^2), t, 0, x )
    for a given x. The integral is approximated by the method
    of trapezoids. Parameters are x, and the number of slices.
    """
    w = x / N  # Width of each trapezoid
    s = 0.5 * f(x) * w + 0.5 * f(0) * w  # Area of first and last trapezoids

    for i in range(1, N):  # Area of rest of trapezoids
        s += f(i * w) * w

    return s


x = np.linspace(-5, 5, 100)
y = []

# With N = 4 trapezoids we already have accuracy of two
# significant figures which is sufficient for plotting.
# For each of the x-values defined above, compute E(x) and add to list y.
for i in x:
    y.append(E(i, 4))


# Plot the results
plt.rc('text', usetex=True)
plt.plot(x, y)
plt.legend([r"$E(x) = \int_0^x e^{-t^2}\,dt$"])
plt.title("Gaussian Error Function")
plt.show()
