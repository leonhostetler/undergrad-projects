#! /usr/bin/env python
"""
Uses the 4th-order Runge-Kutta method to solve the
pair of coupled differential equations
    dP/dt = -P/p
    dD/dt = P/p - D/d
where P(t) and D(t) are both functions of time.

Leon Hostetler, Mar. 31, 2017

USAGE: rad_decay_coupled.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


def rk4(func, r, t, h, tau):
    """
    Runge-Kutta 4 method for solving 1st order differential equations

    Usage: xNew = rk4(func, r, t, h)

    Given a function  f(x, t, h) = dx/dt and initial starting
    conditions for x, rk4() returns the next values of x.
    func:  user defined function for the 1st order differential equations
    r: dependent variable
    t: independent variable
    h: independent variable step value
    """
    k1 = h*func(r, t, tau)
    k2 = h*func(r + 0.5*k1, t + 0.5*h, tau)
    k3 = h*func(r + 0.5*k2, t + 0.5*h, tau)
    k4 = h*func(r+k3, t+h, tau)
    return (k1 + 2*k2 + 2*k3 + k4)/6


def f(r, t, tau):
    """
    Defines the set of coupled differential equations as a single
    vectorized function.
    """
    P = r[0]
    D = r[1]
    fP = -P/2.0
    fD = P/2.0 - D/tau

    return np.array([fP, fD], float)


def compute_and_plot(tau, markstyle, flag=False):

    """
    The flag parameter allows me to turn on and off the plotting
    of N_P(t) which does not depend on tau_D.
    """

    tMin, tMax, h = 0.0, 15.0, 0.01
    tPoints = np.arange(tMin, tMax, h)
    PPoints, DPoints = [], []

    # Set initial conditions
    P0, D0 = 1.0, 0.0
    r = np.array([P0, D0], float)

    # Solve
    for t in tPoints:
        PPoints += [r[0]]
        DPoints += [r[1]]
        r += rk4(f, r, t, h, tau)

    # Only plot N_P(t) the first time around
    if flag is True:
        plabel = r"$N_P(t)$"
        plt.plot(tPoints, PPoints, label=plabel)

    dlabel = r"$N_D(t), \,\tau_D = " + str(tau) + "$ s"
    plt.plot(tPoints, DPoints, label=dlabel, marker=markstyle,
             markevery=30, linestyle="none")


#
# Main
#

plt.rc('text', usetex=True)
plt.title(r"Radioactive Decay of Parent and Daughter Nuclei")

# Compute and plot the solutions for N_D(t) for various tau_D
compute_and_plot(0.02, "x", flag=True)
compute_and_plot(2.0, "+")
compute_and_plot(200.0, "*")

plt.legend(loc=1)
plt.xlabel(r"$t$")
plt.show()
