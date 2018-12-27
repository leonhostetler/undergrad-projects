#! /usr/bin/env python
"""

Approximate the derivative of a function at a given point using several different methods.
I plot the derivative of f(x) = x^(4/3) along with four different numerical approximations
    of its derivative. 

Leon Hostetler, Feb. 4, 2017

USAGE: python derivative_approx.py

"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt


x = 1.0  # Number of terms in the polynomial approximations
res = 10000  # Plotting resolution
left = 0.001   # Graph bounds
right = 5.0
#top = 1.0
#bottom = -1.0


# Generate the x-values
X = np.linspace(left, right, res)


###########################################################
#  Approximation 1: M_1(x) = [f(x+h) - f(x)] / h
###########################################################
def M1(x, h):
    return ((((x+h)**4)**(1/3))-((x**4)**(1/3)))/h

# Evaluate for all x in the linspace defined above.
YM1 = []
for h in X:
    YM1.append(M1(x, h))


###########################################################
#  Approximation 2: M_2(x) = [f(x+h) - f(x-h)] / (2h)
###########################################################
def M2(x, h):
    return ((((x+h)**4)**(1/3))-(((x-h)**4)**(1/3)))/(2*h)

# Evaluate for all x in the linspace defined above.
YM2 = []
for h in X:
    YM2.append(M2(x, h))


###########################################################
#  Approximation 3: M_3(h) = [-f(x+2h) + 4f(x+h) - 3f(x)] / (2h)
###########################################################
def M3(x, h):
    return (-(((x+2*h)**4)**(1/3)) + 4*(((x+h)**4)**(1/3)) - 3*((x**4)**(1/3)))/(2*h)

# Evaluate for all x in the linspace defined above.
YM3 = []
for h in X:
    YM3.append(M3(x, h))


###########################################################
#  Approximation 4: M_4(h) = [f(x-2h) - 4f(x-h) + 3f(x)] / (2h)
###########################################################
def M4(x, h):
    return ((((x-2*h)**4)**(1/3)) - 4*(((x-h)**4)**(1/3)) + 3*((x**4)**(1/3)))/(2*h)

# Evaluate for all x in the linspace defined above.
YM4 = []
for h in X:
    YM4.append(M4(x, h))


###########################################################
#  TRUE FUNCTION
###########################################################
def fun(x):  # Define the true function here
    return (4/3)*(x**(1/3))

Y = np.array([fun(x) for i in X])  # Compute the y-values for the true function

###########################################################
#  ERROR ANALYSIS
###########################################################

# Given a list of x-values, a list of y-values, and a
# a parameter r that defines the weight of the weighted average,
# this function returns a list of x values and a list of y values
# for a smoothed curve.
def smooth_the_curve(inputX, inputY, r):
    smoothX = inputX[r:len(inputX)-r]
    smoothY = []
    for k in range(r, len(inputX)-r):
        avg = 0
        for m in range(k - r, k+r+1):
            avg += inputY[m]
        smoothY.append(avg/(2*r+1))
    return smoothX, smoothY

M1Error = [abs(a - b) for a, b in zip(Y, YM1)]
M2Error = [abs(a - b) for a, b in zip(Y, YM2)]
M3Error = [abs(a - b) for a, b in zip(Y, YM3)]
M4Error = [abs(a - b) for a, b in zip(Y, YM4)]

smoothedM1Error = smooth_the_curve(X, M1Error, 50)
smoothedM2Error = smooth_the_curve(X, M2Error, 50)
smoothedM3Error = smooth_the_curve(X, M3Error, 50)
smoothedM4Error = smooth_the_curve(X, M4Error, 50)

print("For the given domain, the critical values of h for M1, M2, M3, and M4, respectively, are:")
print(smoothedM1Error[0][np.argmin(smoothedM1Error[1])])
print(smoothedM2Error[0][np.argmin(smoothedM2Error[1])])
print(smoothedM3Error[0][np.argmin(smoothedM3Error[1])])
print(smoothedM4Error[0][np.argmin(smoothedM4Error[1])])


###########################################################
# PLOT THE RESULTS
###########################################################
plt.rc('text', usetex=True)
fig, ax = plt.subplots()
plot1, = ax.plot(X, Y)  # True function
plot2, = ax.plot(X, YM1)
plot3, = ax.plot(X, YM2)
plot4, = ax.plot(X, YM3)
plot5, = ax.plot(X, YM4)
ax.legend([plot1,
           plot2,
           plot3,
           plot4,
           plot5,
           ],
          [r'$\frac{d}{dx}f(x)$',
           r'$M_1(h)$',
           r'$M_2(h)$',
           r'$M_3(h)$',
           r'$M_4(h)$',
           ])
ax.grid()
axes = plt.gca()
plt.title(r'Derivative Approximation of $f(x) = x^{\frac43}$')
axes.set_xlim([left, right])
#axes.set_ylim([bottom, top])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
#plt.show()

fig, ax = plt.subplots()
#plot1, = ax.plot(X, M1Error)  # Absolute error
#plot2, = ax.plot(X, M2Error)  # Absolute error
#plot3, = ax.plot(X, M3Error)  # Absolute error
#plot4, = ax.plot(X, M4Error)  # Absolute error
plot12, = ax.plot(smoothedM1Error[0], smoothedM1Error[1])  # Weighted average
plot22, = ax.plot(smoothedM2Error[0], smoothedM2Error[1])  # Weighted average
plot32, = ax.plot(smoothedM3Error[0], smoothedM3Error[1])  # Weighted average
plot42, = ax.plot(smoothedM4Error[0], smoothedM4Error[1])  # Weighted average
ax.legend([plot12,
           plot22,
           plot32,
           plot42,
           ],
          [r'$M_1(h)$ Error',
           r'$M_2(h)$ Error',
           r'$M_3(h)$ Error',
           r'$M_4(h)$ Error',
           ])
ax.grid()
axes = plt.gca()
plt.title('Smoothed Error')
#axes.set_xlim([left, right])
#axes.set_ylim([-1.0, 1.0])
#axes.set_ylim([0.0, 1e-10])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.show()
