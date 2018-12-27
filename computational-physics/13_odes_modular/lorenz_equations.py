#! /usr/bin/env python
"""
The Lorenz equations are the system of first order ODEs:

    dx/dt = sigma*(y-x)
    dy/dt = rho*x - y - xz
    dz/dt = xy - bz

lorenz_equations.py solves this system of ODEs using the fourth-order Runge-Kutta
method.

Leon Hostetler, Apr. 9, 2017

USAGE: python lorenz_equations.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import mymodule_ODEs as mmo
import numpy as np


def f(r, t):
    """
    Write the set of first-order ODEs
        dx/dt = sigma*(y-x)
        dy/dt = rho*x - y - xz
        dz/dt = xy - bz
    as a single vectorized function of the form
        f(r,t) = dr/dt
    where
        f(x,t) = dx/dt, f(y,t) = dy/dt, f(z,t) = dz/dt
    """
    sigma = 10
    rho = 28
    b = 8/3

    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma*(y-x)
    fy = rho*x - y - x*z
    fz = x*y - b*z

    return np.array([fx, fy, fz], float)


# Constants
tMin, tMax, N = 0.0, 50.0, 5000
h = (tMax - tMin)/N

# Create a Runge-Kutta object, and pass our function to it.
rk = mmo.RungeKutta(f)

# The list of points for time, x(t), and y(t)
tPoints = np.arange(tMin, tMax, h)
xPoints, yPoints, zPoints = [], [], []

# Initialize the list (of lists) of function values with the initial conditions
r = np.array([0, 1, 0], float)

# Apply the Runge-Kutta method
for t in tPoints:
    xPoints += [r[0]]
    yPoints += [r[1]]
    zPoints += [r[2]]
    r += rk(r, t, h)

# Display the results
plt.rc('text', usetex=True)

plt.figure(1)
plt.subplot(211)
plt.title(r"Numerical Solutions of the Lorenz Equations")
plt.plot(tPoints, yPoints)
plt.xlabel(r"$t$")
plt.ylabel(r"$y(t)$")

plt.subplot(212)
plt.plot(xPoints, zPoints)
plt.xlabel(r"$x$")
plt.ylabel(r"$z(x)$")
plt.show()
