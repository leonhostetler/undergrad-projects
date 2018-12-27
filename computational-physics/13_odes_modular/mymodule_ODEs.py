#! /usr/bin/env python
"""
Module mymodule_ODEs.py is a module containing a collection of user-defined
classes and functions for working with ordinary differential equations.

Leon Hostetler, Apr. 9, 2017

USAGE: To be used as a supplement to a main program.
"""

from __future__ import division, print_function


class RungeKutta:
    """
    This class declares the Runge-Kutta object which can be used to
    solve systems of ODEs using the fourth order Runge-Kutta method.

    Symbols and parameters:

    'function' is a user-defined function.
    'r' is a scalar or vector passed to the Runge-Kutta method.
    't' is the time
    'h' is the time step

    """

    def __init__(self, function):
        self.func = function
        self.order = 4  # The order of the Runge-Kutta method

    def __call__(self, r, t, h):
        k1 = h*self.func(r, t)
        k2 = h*self.func(r + 0.5*k1, t + 0.5*h)
        k3 = h*self.func(r + 0.5*k2, t + 0.5*h)
        k4 = h*self.func(r + k3, t + h)
        return (k1 + 2*k2 + 2*k3 + k4)/6
