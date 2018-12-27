#! /usr/bin/env python
"""
The Lotka-Volterra equations are a mathematical predator-prey model consisting
of the pair of first-order coupled differential equations
    dx/dt = alpha*x - beta*x*y
    dy/dt = gamma*x*y - delta*y

lotka_volterra.py solves this system of ODEs using the fourth-order Runge-Kutta
method.

Leon Hostetler, Apr. 9, 2017

USAGE: python lotka_volterra.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import mymodule_ODEs as mmo
import numpy as np


def f(r, t):
    """
    Write the set of first-order ODEs
        dx/dt = alpha*x - beta*x*y
        dy/dt = gamma*x*y - delta*y
    as a single vectorized function of the form
        f(r,t) = dr/dt
    where
        f(x,t) = dx/dt, f(y,t) = dy/dt.
    """
    alpha = 1
    beta = 0.5
    gamma = 0.5
    delta = 2

    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y - delta*y

    return np.array([fx, fy], float)


# Constants
tMin, tMax, N = 0.0, 30.0, 1000
h = (tMax - tMin)/N

# Create a Runge-Kutta object, and pass our function to it.
rk = mmo.RungeKutta(f)

# The list of points for time, x(t), and y(t)
tPoints = np.arange(tMin, tMax, h)
xPoints, yPoints = [], []

# Initialize the list (of lists) of function values with the initial conditions
r = np.array([2, 2], float)

# Apply the Runge-Kutta method
for t in tPoints:
    xPoints += [r[0]]
    yPoints += [r[1]]
    r += rk(r, t, h)

# Plot the numerical solutions of x(t) and y(t)
plt.rc('text', usetex=True)
plt.title(r"Numerical Solutions of the Lotka-Volterra Model")
plt.plot(tPoints, xPoints, label=r"$x(t)$")
plt.plot(tPoints, yPoints, 'g--', label=r"$y(t)$")
plt.legend(loc=1)
plt.xlabel(r"$t$")
plt.show()
