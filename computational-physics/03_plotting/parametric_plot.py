#! /usr/bin/env python
"""
Plot the deltoid curve parametrically.

Leon Hostetler, Feb. 3, 2017

USAGE: parametric_plot.py
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

# Main body of program

# Define the theta values, and give the parametric equations for x and y
theta = np.linspace(0, 2*np.pi)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

# Plot the results
plt.rc('text', usetex=True)
plt.plot(x, y)
plt.text(1.5, 2, r"\begin{eqnarray*}"
                 r"x &=& 2 \cos \theta + \cos(2\theta)\\"
                 r"y &=& 2 \sin \theta - \sin(2\theta)"
                 r"\end{eqnarray*}",
         bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
plt.title("Parametric Deltoid Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("deltoid_curve.png")
plt.show()
