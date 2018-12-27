#! /usr/bin/env python
"""
Module My Module Integration is a module containing a collection of user-defined
functions for numerical integration.

Symbols and parameters:

    'f' is a user-defined function e.g. f(x) = x**2. For the multi-
        dimensional monte carlo method, f is a multi-dimensional function
        e.g. f(x) = x[0]**2 + x[1]**2.
    'lower' is the lower bound on the integral
    'upper' is the upper bound on the integral
    'N' is the number of slices for the trapezoidal and simpson methods.
        For the monte carlo methods, N is the number of random points.
    'accuracy' is the minimum accuracy you want.
    'detailed' if 'True' prints detailed results during integration.
    'dim' for the multi-dimensional monte carlo method is the number of dimensions
    'limit' for the monte carlo method is the integration limits. E.g in the
        2D case, you would have your limits as [[-1, 1], [-1, 1]] if both inner
        and outer integrals go from -1 to 1.

Leon Hostetler, Mar. 8, 2017

USAGE: To be used as a supplement to a main program.
"""

from __future__ import division, print_function
import numpy.random as rnd
import numpy as np
import sys


def integrate_trapz(f, lower, upper, N=1000):
    """
    Integrate the function from lower to upper using
    trapezoidal integration.

    Takes in the function, the lower and upper limits of integration,
    and the number of trapezoidal slices to use.
    """
    a = lower           # Lower integration limit
    b = upper           # Upper integration limit
    w = (b - a) / N     # Width of each trapezoid

    # Area of first and last trapezoids
    I = 0.5 * f(a) * w + 0.5 * f(b) * w

    # Area of rest of trapezoids
    for i in range(1, N):
        I += f(a + i * w) * w

    return I, N


def integrate_simpson(f, lower, upper, N=1000):
    """
    Integrate the function from lower to upper using
    simpson integration.

    Takes in the function, the lower and upper limits of integration,
    and the number of slices to use.
    """
    a = lower           # Lower integration limit
    b = upper           # Upper integration limit
    w = (b - a) / N     # Width of each trapezoid

    if N % 2 != 0:
        N += 1
        print("Number of slices was odd so 1 was added to N.")

    I = (1 / 3) * f(a) * w + (1 / 3) * f(b) * w  # Area of first and last trapezoids

    for i in range(1, N, 2):  # Odd terms
        I += f(a + i * w) * w * (4 / 3)

    for i in range(2, N, 2):  # Even terms
        I += f(a + i * w) * w * (2 / 3)

    return I, N


def integrate_trapz_adaptive(f, lower, upper, accuracy=1e-8, detailed=False):
    """
    Integrate the function from lower to upper using adaptive
    trapezoidal integration.

    Send the 'detailed' parameter with a value of 'True' if you
    want to print results for every N that is evaluated.
    """
    a = lower       # Lower limit of integration
    b = upper       # Upper limit of integration
    Tol = accuracy  # Error tolerance
    error = 1       # Error needs to be initialized as something
    N = 1           # Start with 1 trapezoid

    # I0 is the approximation with a single trapezoid
    I0 = (f(a) + f(b))*(b-a)*0.5

    # Do you want detailed results?
    if detailed is True:
        print("N = ", N, ", I = ", I0, sep="")

    while error > Tol:      # Repeat until the error is less than the error tolerance

        N *= 2              # Double the slices each iteration
        w = (b - a)/N       # Width of each trapezoid

        I = 0.5*I0
        for i in range(1, N, 2):
            I += f(a + i*w)*w

        error = abs(I - I0)/3

        I0 = I

        # Do you want detailed results?
        if detailed is True:
            print("N = ", N, ", I = ", I, ", Error = ", error, sep="")

    return I, N, error


def integrate_simpson_adaptive(f, lower, upper, accuracy=1e-15, detailed=False):
    """
    Integrate the function from lower to upper using adaptive
    simpson integration.

    Send the 'detailed' parameter with a value of 'True' if you
    want to print results for every N that is evaluated.
    """
    a = lower       # Lower limit of integration
    b = upper       # Upper limit of integration
    Tol = accuracy  # Error tolerance
    error = 1.0     # Error needs to be initialized as something
    N = 1           # Start with 1 slice

    # I0 is the approximation with a single slice
    I0 = ((b-a)/6) * (f(a) + 4 * f((b - a)/2) + f(b))  # Area of first and last slice

    # Do you want detailed results?
    if detailed is True:
        print("N = ", N, ", I = ", I0, sep="")

    while error > Tol:

        N *= 2
        w = (b - a) / N  # Width of each slice

        I = 0.5 * I0
        for i in range(1, N, 2):
            I += -f(a + w * i) * w / 3
        for i in range(0, N):
            I += (2 / 3) * f(a + w * (i + 1 / 2)) * w

        error = abs(I - I0)/15

        I0 = I

        # Do you want detailed results?
        if detailed is True:
            print("N = ", N, ", I = ", I, ", Error = ", error, sep="")

    return I, N, error


def integrate_monte_carlo(f, lower, upper, N=100):
    """
    Integrate a 1D function f from x = lower to x = upper using the
    Monte Carlo mean value method with N random points.
    """
    a = lower  # Lower limit of integration
    b = upper  # Upper limit of integration

    s = 0
    for i in range(1, N):
        x = a + (b - a) * rnd.random()
        s += f(x)

    I = (b-a)*s/N

    return I


def integrate_monte_carlo_nd(f, dim, limit, N=1000000):
    """
    Integrate an n-dimensional function using the Monte Carlo mean-value
    method. Takes in the parameters: integrand, dimensions, limits of
    integration, and the number of Monte Carlo points.
    """
    I, sum = 1/N, 0
    for n in range(dim):
        I *= (limit[n][1] - limit[n][0])

    for k in range(N):
        x = []
        for n in range(dim):
            x += [limit[n][0] + (limit[n][1] - limit[n][0])*rnd.random()]

        sum += f(x)
    return I*sum


def f(x):
    """
    Define
        f(x) = x^2
    to test the integration methods.
    """
    return x**2


def g(x):
    """
    A 3D function to test the multi-dimensional Monte Carlo method.
    """
    if x[0]**2 + x[1]**2 + x[2]**2 <= 1:
        gx = 1
    else:
        gx = 0

    return gx


def test_functions():
    """
    This function tests the various numerical integration functions in this module.
    To execute test of function run module as python program along with commandline
    argument "test" example: "mypython test"
    """

    isGood = True

    # Test the trapezoidal integration function
    trapz = integrate_trapz(f, 0, 1, N=1000)[0]
    if abs(trapz - 1/3) > 0.00001:
        print("WARNING: integrate_trapz() failed the test.")
        isGood = False

    # Test the simpson integration function
    simps = integrate_simpson(f, 0, 1, N=1000)[0]
    if abs(simps - 1 / 3) > 1e-12:
        print("WARNING: integrate_simpson() failed the test.")
        isGood = False

    # Test the adaptive trapezoidal integration function
    trapz = integrate_trapz_adaptive(f, 0, 1, 1e-12)[0]
    if abs(trapz - 1 / 3) > 1e-12:
        print("WARNING: integrate_trapz_adaptive() failed the test.")
        isGood = False

    # Test the adaptive simpson integration function
    simps = integrate_simpson_adaptive(f, 0, 1, 1e-12)[0]
    if abs(simps - 1 / 3) > 1e-12:
        print("WARNING: integrate_simpson_adaptive() failed the test.")
        isGood = False

    # Test the 1D Monte Carlo integration function
    monte = integrate_monte_carlo(f, 0, 1, 1000000)
    if abs(monte - 1 / 3) > 0.01:
        print("WARNING: integrate_monte_carlo() failed the test.")
        print("NOTE: There is a small probability of random failure with this method.")
        print("Run the test a few more times.")
        isGood = False

    # Test the multi-dimensional Monte Carlo integration function
    monte = integrate_monte_carlo_nd(g, 3, [[-1, 1], [-1, 1], [-1, 1]], N=100000)
    if abs(monte - (4/3)*np.pi) > 0.1:
        print("WARNING: integrate_monte_carlo_nd() failed the test.")
        print("NOTE: There is a small probability of random failure with this method.")
        print("Run the test a few more times.")
        isGood = False

    if isGood is True:
        print("Module is good.")


# TEST BLOCK
# The test block only executes if the module is run as a main program
# and if the word "test" is given on the command line.
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_functions()
