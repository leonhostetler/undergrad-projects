#! /usr/bin/env python
"""
Numerically approximates the solution to the differential equation
    dN/dt = -N/tau
using the difference equation
    N[i+1] = (1 - h/tau)N[i].
The results using different values of tau are compared to the exact solution
    N(t) = N0*exp(-t/tau)
by plotting them together on a single graph.

Leon Hostetler, Mar. 31, 2017

python rad_decay_taus.py
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np


def plot_exact_and_approx(t0, tmax, N0, h, tau, mark=1):
    """
    Plot the exact and numerically approximated solutions for a given
    value of tau and h. The 'mark' parameter modifies the number of points that
    are plotted for the approximate solution. I.e. mark = 50 means only
    every 50th point is plotted. This prevents the plots from obscuring
    other plots beneath them.
    """
    tlist = np.linspace(t0, tmax)
    Nlist = [N0*np.exp(-t/tau) for t in tlist]

    tpoints = [t0]
    Npoints = [N0]

    for i, t in enumerate(np.arange(h, tmax, h)):
        tpoints += [t]
        Npoints += [Npoints[i] - h*Npoints[i]/tau]

    # Plots the exact solution as a solid line and the numerically
    # approximated solution as x's.
    exactlabel = r"$N(t) = N_0 e^{-\frac{t}{" + str(tau) + "s}}$"
    approxlabel = r"$\tau = " + str(tau) + ", \, h = " + str(h) + "$ s"

    plt.plot(tlist, Nlist, label=exactlabel)
    plt.plot(tpoints, Npoints, linestyle="none",
             marker="x", markevery=mark, label=approxlabel)


# Plot the results
plt.rc('text', usetex=True)
plt.title("Exact vs. Approximated Solutions for Various Tau")

plot_exact_and_approx(0.0, 15.0, 1.0, 0.01, 5.0, 50)
plot_exact_and_approx(0.0, 15.0, 1.0, 0.01, 3.0, 50)
plot_exact_and_approx(0.0, 15.0, 1.0, 0.01, 1.0, 50)

plt.legend(loc=1)
plt.xlabel(r"$t$")
plt.show()

# NOTE: For tau = 0.1 and 0.01, the decay rate is too high to display nicely
# with the other values of tau, so I am putting the last two on a separate graph
# with 0.0 < t < 0.3.
plt.rc('text', usetex=True)
plt.title("Exact vs. Approximated Solutions for Various Tau")

plot_exact_and_approx(0.0, 0.3, 1.0, 0.01, 0.1)
plot_exact_and_approx(0.0, 0.3, 1.0, 0.01, 0.01)

plt.legend(loc=1)
plt.xlabel(r"$t$")
plt.show()
