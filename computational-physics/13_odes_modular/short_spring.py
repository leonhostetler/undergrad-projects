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

USAGE: python short_spring.py
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
B, b = 7, 6
tMin, tMax, N = 0.0, 50*np.pi, 5000
h = (tMax - tMin)/N

# Create a Runge-Kutta object, and pass our function to it.
rk = mmo.RungeKutta(f)

# The list of points for time, x(t), and y(t)
tPoints = np.arange(tMin, tMax, h)
xPoints, yPoints = [], []

# Initialize the list (of lists) of function values with the initial conditions
r = np.array([3, 0], float)

# Apply the Runge-Kutta method
for t in tPoints:
    xPoints += [r[0]]
    yPoints += [r[1]]
    r += rk(r, t, h)


# Display the results
plt.rc('text', usetex=True)

plt.figure(1)
plt.subplot(211)
title = "Short Spring Displacement and Phase Space for $B = " + str(B) + "$ and $b = " + str(b) + "$."
plt.title(title)
plt.plot(tPoints, xPoints)
plt.xlabel(r"$t$")
plt.ylabel(r"$x(t)$")

plt.subplot(212)
plt.plot(xPoints, yPoints)
plt.xlabel(r"$x$")
plt.ylabel(r"$\frac{dx}{dt}$")
plt.show()
