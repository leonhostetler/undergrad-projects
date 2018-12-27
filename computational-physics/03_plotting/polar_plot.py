#! /usr/bin/env python
"""
Plot a polar function by converting to cartesian coordinates.

Leon Hostetler, Feb. 3, 2017

USAGE: polar_plot.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

# Main body of program

theta = np.linspace(0, 10*np.pi, 1000)  # The values of theta
r = theta**2                            # The function r = f(theta)
x = r*np.cos(theta)                     # Convert to cartesian coordinates
y = r*np.sin(theta)


# Plot the results
plt.rc('text', usetex=True)
plt.plot(x, y)
plt.legend([r"$r = \theta^2$"])
plt.title("Polar Galilean Spiral")
plt.savefig("polar_plot.png")
plt.show()
