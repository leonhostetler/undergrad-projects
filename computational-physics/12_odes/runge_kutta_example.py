#! /usr/bin/env python
"""
The fourth-order Runge-Kutta method is a standard method for solving
a system of coupled first-order ordinary differential equations.

Leon Hostetler, Apr. 9, 2017

USAGE: python runge_kutta_example.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


def rk4(func, r, t, h):
    """
    4th order Runge-Kutta method for solving 1st order differential equations

    Given a function  f(x, t, h) = dx/dt and initial starting
    conditions for x, rk4() returns the next values of x.

    func:  user defined function for the 1st order differential equations
    r: dependent variable
    t: independent variable
    h: independent variable step value
    """
    k1 = h*func(r, t)
    k2 = h*func(r + 0.5*k1, t + 0.5*h)
    k3 = h*func(r + 0.5*k2, t + 0.5*h)
    k4 = h*func(r+k3, t+h)
    return (k1 + 2*k2 + 2*k3 + k4)/6


def f(r, t):
    """
    Write your set of differential equations
        dx/dt, dy/dt
    as a single vectorized function of the form
        f(r,t) = dr/dt
    where
        f(x,t) = dx/dt, f(y,t) = dy/dt.
    """

    x = r[0]
    y = r[1]
    fx = x*y - x
    fy = y - x*y + np.sin(t)**2

    return np.array([fx, fy], float)


# Constants
tMin, tMax, N = 0.0, 10.0, 1000
h = (tMax - tMin)/N

# The list of points for time, x(t), and y(t)
tPoints = np.arange(tMin, tMax, h)
xPoints, yPoints = [], []

# Initialize the list (of lists) of function values with the initial conditions
r = np.array([1.0, 1.0], float)

# Apply the Runge-Kutta method
for t in tPoints:
    xPoints += [r[0]]
    yPoints += [r[1]]
    r += rk4(f, r, t, h)

# Plot the numerical solutions of x(t) and y(t)
plt.rc('text', usetex=True)
plt.title(r"Numerical Solutions of $\frac{dx}{dt}$ and $\frac{dy}{dt}$")
plt.plot(tPoints, xPoints, label=r"$x(t)$")
plt.plot(tPoints, yPoints, label=r"$y(t)$")
plt.legend(loc=1)
plt.xlabel(r"$t$")
plt.show()
