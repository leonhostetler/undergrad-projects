#! /usr/bin/env python
"""
Compute the volume of an n-dimensional hypersphere
using the Monte Carlo mean-value method.

The volume is computed for hyperspheres with dimensions from 0 to 12
and plotted.

Leon Hostetler, Mar. 7, 2017

USAGE: python hypersphere_volume.py
"""

from __future__ import division, print_function
import mymodule_integration as mmi
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """
    The integrand of the integral being evaluated.
    """
    s = 0
    for k in range(dim):
        s += x[k]**2

    if s <= 1:
        fx = 1
    else:
        fx = 0

    return fx


x = np.arange(0, 13)    # x-values
y = []                  # y-values


for k in range(13):
    dim = k

    # For every dimension, the limit of integration is [-1, 1]
    limit = []
    for i in range(dim):
        limit.append([-1, 1])

    # Compute the integral for this dimension
    integral = mmi.integrate_monte_carlo_nd(f, dim, limit)
    print("The ", k, "-dimensional hypersphere has volume ", integral, ".", sep="")
    y.append(integral)


# Plot the results
plt.rc('text', usetex=True)
plt.plot(x, y)
plt.title("Volume of n-dimensional Unit Hypersphere")
plt.xlabel("Dimension")
plt.ylabel("Volume")
plt.show()
