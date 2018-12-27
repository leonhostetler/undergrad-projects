"""
This program numerically approximates the solution to
    dN/dt = -N/tau
where N is a function of t. The solution is approximated using
the difference equation
    N[i+1] = (1 - h/tau)N[i]
where h is a small number. The exact solution is easily found to be
    N(t) = exp(-t/tau)
so we can compare the exact solution with the numerically
approximated solution by plotting the two.
In this example, we have h = 0.01s, and 0.0 < t < 15.0 seconds.

Leon Hostetler, Apr. 9, 2017

USAGE: python eulers_method_example.py
"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np

h, tmax = 0.01, 15.0

# Create lists to store the t and N(t) values for the numerically
# approximated solution. Initialize the lists with your initial values.
t_list = [0.0]
N_list = [1.0]

# Euler's method
i = 0
for t in np.arange(h, tmax, h):
    t_list += [t]
    N_list += [N_list[i] - 0.5*h*N_list[i]]
    i += 1

# Plot the results
plt.title("Numerical Approximation of N(t)")
plt.plot(t_list, N_list)
plt.xlabel("t")
plt.ylabel("N(t)")
plt.show()
