#! /usr/bin/env python
"""
Solves the initial value ODE of the form

    dy/dt = f(y,t)

with the initial condition y(0) = y_0. It is solved using the fourth-order
Runge-Kutta method.

Leon Hostetler, Mar. 2017

USAGE: python ode_rk4.py

"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


def f(y, t):
    return y + 1


T = 1               # Final time
N = 10              # Number of time slices

y_list = [1.0]      # Initial value
t_list = [0.0]      # Initial time
dt = T/N            # Time step
for i in range(N):
    k1 = dt*f(y_list[i], i*dt)
    k2 = dt*f(y_list[i] + k1/2, i*dt + dt/2)
    k3 = dt*f(y_list[i] + k2/2, i*dt + dt/2)
    k4 = dt*f(y_list[i] + k3, i*dt + dt)
    y_list += [y_list[i] + (k1 + 2*k2 + 2*k3 + k4)/6]
    t_list += [t_list[i] + dt]


# This is the exact solution
t_list2 = np.linspace(0, T, 1000)
exact_y = 2*np.exp(t_list2) - 1

# Plot the results
plt.rc('text', usetex=True)
plt.title("A Plot of Multiple Functions")
plt.plot(t_list2, exact_y, label=r"$y(t) = 2e^t - 1$")
plt.plot(t_list, y_list, label="Approx.")
plt.legend(loc=2)
plt.xlabel(r"$t$")
plt.show()
