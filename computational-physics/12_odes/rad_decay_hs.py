#! /usr/bin/env python
"""
Numerically approximates the solution to the differential equation
    dN/dt = -N/tau
using the difference equation
    N[i+1] = (1 - h/tau)N[i].
The results using different values of h are compared to the exact solution
    N(t) = N0*exp(-t/tau)
by plotting them together on a single graph.

Leon Hostetler, Mar. 31, 2017

USAGE: python rad_decay_hs.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


# Constants
N0, tmax, tau = 1.0, 15.0, 2.0

# The t and N(t) values for the exact solution.
tlist = np.linspace(0.0, tmax)
Nlist = [np.exp(-t/tau) for t in tlist]


t1points = [0]
N1points = [N0]  # at t=0, N(t) = 100%
h = 1.0
for i, t in enumerate(np.arange(h, tmax, h)):
    t1points += [t]
    N1points += [N1points[i] - h*N1points[i]/tau]


t2points = [0]
N2points = [N0]  # at t=0, N(t) = 100%
h = 0.1
for i, t in enumerate(np.arange(h, tmax, h)):
    t2points += [t]
    N2points += [N2points[i] - h*N2points[i]/tau]


t3points = [0]
N3points = [N0]  # at t=0, N(t) = 100%
h = 0.01
for i, t in enumerate(np.arange(h, tmax, h)):
    t3points += [t]
    N3points += [N3points[i] - h*N3points[i]/tau]


# Plot the exact solution vs. the approximated solutions
plt.rc('text', usetex=True)
plt.title("Exact vs. Approximated Solutions")
plt.plot(tlist, Nlist, label=r"$N(t) = N_0 e^{-\frac{t}{\tau}}$")
plt.plot(t1points, N1points, linestyle="none",
         marker="x", label=r"$h = 1.0$ s")
plt.plot(t2points, N2points, linestyle="none",
         marker="x", markevery=5, label=r"$h = 0.1$ s")
plt.plot(t3points, N3points, linestyle="none",
         marker="x", markevery=50, label=r"$h = 0.01$ s")
plt.legend(loc=1)
plt.xlabel(r"$t$")
plt.show()


# Compute the fractional error for each case.
error1 = [np.abs((np.exp(-t/tau) - N1points[i])/np.exp(-t/tau))
          for i, t in enumerate(t1points)]
error2 = [np.abs((np.exp(-t/tau) - N2points[i])/np.exp(-t/tau))
          for i, t in enumerate(t2points)]
error3 = [np.abs((np.exp(-t/tau) - N3points[i])/np.exp(-t/tau))
          for i, t in enumerate(t3points)]


# Plot another graph, this one displaying the fractional error
# for each approximated solution.
plt.rc('text', usetex=True)
plt.title("Fractional Error")
plt.plot(t1points, error1, label=r"Error for $h = 1.0$ s")
plt.plot(t2points, error2, label=r"Error for $h = 0.1$ s")
plt.plot(t3points, error3, label=r"Error for $h = 0.01$ s")
plt.legend(loc=2)
plt.xlabel(r"$t$")
plt.show()
