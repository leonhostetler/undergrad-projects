#! /usr/bin/env python
"""

Compare the precision of brute force polynomial evaluation with Horner's method.

Leon Hostetler, Feb. 4, 2017

USAGE: python polynomial_evaluation.py

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

N = 200  # Number of terms in the polynomial approximations

lower = 1       # Lower limit on sum
upper = 50      # Upper limit on sum
res = 1000      # Plotting resolution
left = -1.0     # Graph bounds
right = 1.2
top = 3.0
bottom = -5.0

# Generate the list of coefficients
a = [0.0]
for i in range(1, N+1):
    a.append(((-1)**(i+1))/i)

# Generate the x-values
X = np.linspace(left, right, res)


#
#  BRUTE FORCE ALGORITHM
#


# Evaluate the polynomial approximation at x using the
# brute force method and return P_N(x).
def brute_force(x):
    y = 0.0
    for k in range(N+1):
        y += a[k]*(x**(k))
    return y

# Generate a list of values P_N(x) using the brute force method
# Evaluate for all x in the linspace defined above.
YBruteForce = []
for i in X:
    YBruteForce.append(brute_force(i))


#
#  HORNER'S ALGORITHM
#

# Evaluate the polynomial approximation at x using
# Horner's method and return P_N(x)
def horner(x):
    y = a[N]
    for k in range(N, 0, -1):
        y = y*x + a[k-1]
    return y

# Generate a list of values P_N(x) using the Horner method
# Evaluate for all x in the linspace defined above.
YHorner = []
for i in X:
    YHorner.append(horner(i))


#
#  DEFINE THE TRUE FUNCTION
#
def fun(x):
    return np.log(1 + x)

XTrue = np.linspace(left+10e-15, right, res)
Y = np.array([fun(i) for i in XTrue])  # Compute the y-values for the true function

#
#  CALCULATE THE ERROR
#

print("The difference between the algorithms:")
C = [a - b for a, b in zip(YBruteForce, YHorner)]
print(C)


#
# PLOT THE RESULTS
#
plt.rc('text', usetex=True)
fig, ax = plt.subplots()
plot1, = ax.plot(XTrue, Y)  # True function
plot2, = ax.plot(X, YBruteForce)
plot3, = ax.plot(X, YHorner)
polyName = "P_{" + str(N) + "}(x)"
ax.legend([plot1,
           plot2,
           plot3,
           ],
          [r'$\log(1+x)$',
           r'$' + polyName + '$ with Brute Force',
           r'$' + polyName + '$ with Horner Method',
           ])
ax.grid()
axes = plt.gca()
plt.title('Polynomial Evaluation Algorithms')
axes.set_xlim([left, right])
axes.set_ylim([bottom, top])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
