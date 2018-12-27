#! /usr/bin/env python
"""
The equation of motion for a short, damped, driven spring is

    d^2x/dt^2 + b(dx/dt) + Ax^3 =  B*cos(omega_d t)

This can be written as the pair of simultaneous first-order ODEs:

    dy/dt = B*cos(omega_d t) - Ax^3 - by
    dx/dt = y

short_spring.py solves this system of ODEs using the fourth-order Runge-Kutta
method.

Leon Hostetler, Apr. 9, 2017

USAGE: python short_spring_poincare.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import mymodule_ODEs as mmo
import numpy as np


def f(r, t):
    """
    Write the set of first-order ODEs
        dy/dt = B*cos(omega_d t) - Ax^3 - by
        dx/dt = y
    as a single vectorized function of the form
        f(r,t) = dr/dt.
    """
    A = 1
    omega_d = 1

    x = r[0]
    y = r[1]
    fx = y
    fy = B*np.cos(omega_d*t) - A*x**3 - b*y

    return np.array([fx, fy], float)


# Constants
# NOTE: tMax = 100000*np.pi produces a very nice Poincare map but takes ~20 minutes
B, b = 7, 0.01
tMin, tMax = 0.0, 1000*np.pi
h = np.pi/180

# Create a Runge-Kutta object, and pass our function to it.
rk = mmo.RungeKutta(f)

# The list of points for time, x(t), and y(t)
tPoints = np.arange(tMin, tMax, h)
xPoints, yPoints = [], []

# Initialize the list (of lists) of function values with the initial conditions
r = np.array([3, 0], float)

# Apply the Runge-Kutta method
i = 0
for t in tPoints:
    if i % 360 == 0:  # Only plot points where t = n*2pi
        xPoints += [r[0]]
        yPoints += [r[1]]
    r += rk(r, t, h)
    i += 1

# Display the results
plt.rc('text', usetex=True)
plt.title("Phase Space")
plt.scatter(xPoints, yPoints, s=1, c='k')
plt.xlabel(r"$x$")
plt.ylabel(r"$\frac{dx}{dt}$")
plt.show()
