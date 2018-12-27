#! /usr/bin/env python
"""
Plot Fay's function (the butterfly curve) by
converting the polar function to cartesian coordinates.

Leon Hostetler, Feb. 3, 2017

USAGE: fays_function.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

# Main body of program

# Theta values
theta = np.linspace(0, 24*np.pi, 10000)

# The polar function
r = np.exp(np.sin(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5

# Convert to cartesian coordinates
x = r*np.cos(theta)
y = r*np.sin(theta)

# Plot the results
plt.rc('text', usetex=True)
plt.plot(x, y)
left, right, bottom, top = plt.axis()
plt.axis((left, right, bottom, top + .75))
plt.legend([r"$r = e^{\sin \theta} - 2 \cos (4 \theta)"
            r" + \sin^5 \left(\frac{\theta}{12}\right)$"])
plt.title("Fay's Function")
plt.savefig("fays_function.png")
plt.show()
