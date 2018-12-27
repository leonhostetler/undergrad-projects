#! /usr/bin/env python
"""
Computes the first several energy eigenvalues and plots the associated
wavefunctions for a given symmetric potential.

Leon Hostetler, Apr. 25, 2017

USAGE: schrodinger.py
"""
from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np
import sys


def V(x, case):
    """
    The symmetric potential. You can change this to compute the
    energy eigenvalues and eigenstates for other symmetric potentials.

    Note: If you add additional choices, you must also add the choice to

        if case not in [1, 2, 3]:
            sys.exit("That was not a valid choice!")

    which is found in the main part of the program.
    """

    if case == 1:
        return x**2
    elif case == 2:
        return np.abs(x)
    elif case == 3:
        if np.abs(x) < 1:
            return 0
        else:
            return np.abs(x)
    if case == 4:  # Harmonic oscillator
        return 0.5*x**2
    if case == 5:  # Infinite square well
        if np.abs(x) < 1:
            return 0
        else:
            return 1e10


def f(r, x, E, vCase):
    """
    Write the set of first-order ODEs
        d(phi)/dx = 2[V(x) - E]psi
        d(psi)/dx = phi
    as a single vectorized function of the form
        f(r,x) = dr/dx.
    """
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = 2*(V(x, vCase) - E)*psi

    return np.array([fpsi, fphi], float)


def rk4(func, r, x, h, E, vCase):
    """
    4th order Runge-Kutta method for solving 1st order differential equations

    func:  user defined function for the 1st order differential equations
    r: dependent variable
    x: independent variable
    h: independent variable step size
    """
    k1 = h*func(r, x, E, vCase)
    k2 = h*func(r + 0.5*k1, x + 0.5*h, E, vCase)
    k3 = h*func(r + 0.5*k2, x + 0.5*h, E, vCase)
    k4 = h*func(r+k3, x+h, E, vCase)
    return (k1 + 2*k2 + 2*k3 + k4)/6


def waveFunction(f, r, xValues, deltaX, E, vCase):
    """
    Solve for the wave function using the 4th order Runge Kuttta method
    to solve for the values for the wavefunction for a given value of the
    energy E.

    Note: The wave function is not necessarily an eigenfunction. It is only
    an eigenfunction if E happens to be an eigenvalue.
    an eigenvalue.
    """
    # make a copy of the initial values so that this function can be
    # repeatedly called with the same initial values
    s = np.copy(r)

    psi = []
    for x in xValues:
        psi += [s[0]]
        s += rk4(f, s, x, h, E, vCase)

    return np.array(psi, float)


def bracketingInterval(E, dE, vCase):
    """
    Given a starting energy and an increment value,
    find a bracketing interval for the energy eigenvalue.
    """
    bracket = False
    while bracket is False:
        E1, E2 = E, E + dE
        psi1 = waveFunction(f, r, xValues, h, E1, vCase)
        psi2 = waveFunction(f, r, xValues, h, E2, vCase)
        if (psi1[-1] < 0) != (psi2[-1] < 0):
            bracket = True

        if E2 > 1000:
            print("Bracketing interval not found!")
            break

        E += dE

    return [E1, E2]


def secantMethod(E1, E2, vCase):
    """
    Given a bracketing interval for the energy eigenvalue,
    find the energy eigenvalue and eigenstate using the secant method.
    """
    target = 1e-6

    while np.abs(E1 - E2) > target:
        # Get the wave function for energy for E1
        psiPoints = waveFunction(f, r, xValues, h, E1, vCase)

        # Get the wavefunction value at the boundary
        psiE1 = psiPoints[-1]

        # Get the wavefunction for energy E2
        psiPoints = waveFunction(f, r, xValues, h, E2, vCase)

        psiE2 = psiPoints[-1]

        # Use the secant method to get new estimates for E1 and E2
        E1, E2 = E2, E2 - psiE2 * (E2 - E1) / (psiE2 - psiE1)

    return [E2, psiPoints]


#######################################################################
#                               MAIN
#######################################################################
case = int(raw_input("Which potential do you want? Enter the appropriate integer"
                     "\n\t1 for V(x) = x^2"
                     "\n\t2 for V(x) = |x|"
                     "\n\t3 for V(|x|<1)=0 and V(|x|>1)=|x|"
                     "\n\t4 for Harmonic Oscillator"
                     "\n\t5 for Infinite Square Well (set plot limit to 1.0001)\n"))

if case not in [1, 2, 3, 4, 5]:
    sys.exit("That was not a valid choice!")

solutions = int(raw_input("How many solutions do you want. E.g. enter 3 if you "
                            "want the ground state and first two excited states: "))

limit = float(raw_input("Enter a plotting limit (E.g. 4): "))


vMin = 0.0  # Minimum potential energy
xMin, xMax, N = 0.0, limit, 1000
h = (xMax - xMin)/N

# The list of x-values
xValues = np.arange(xMin, xMax, h)

# Initialize the plot
plt.rc('text', usetex=True)
plt.title("Numerical Solutions of 1D Schrodinger Equation")


parity = 0  # Ground state is parity even for even V(x)
currentE = vMin  # Ground state energy must be greater than vMin
for solutions in range(solutions):

    # Set the initial conditions, which depend on the parity
    if parity % 2 == 0:
        r = np.array([1.0, 0.0], float)
    else:
        r = np.array([0.0, 1.0], float)

    # Find a bracketing interval. If the energy levels are very
    # closely spaced, you may need to decrease the increment from
    # 0.1 to something smaller.
    interval = bracketingInterval(currentE, 0.1, case)
    E1, E2 = interval[0], interval[1]

    # Solve for the eigenvalue and wavefunction using the secant method
    solution = secantMethod(E1, E2, case)
    E, psi = solution[0], solution[1]

    # Extend the wavefunction to x < 0 using the symmetry of V(x)
    if parity % 2 == 0:
        psi = np.append(psi[::-1], psi[1:])
    else:
        psi = np.append(-psi[::-1], psi[1:])

    # Normalize the wavefunction
    norm = np.sqrt(np.dot(psi, psi)*h)
    psiN = psi/norm

    # Plot the normalized wavefunction
    x = np.append(-xValues[::-1], xValues[1:])
    label = r"$\psi_" + str(parity) + "(x)$"
    plt.plot(x, psiN, label=label)

    print("\nState", parity)
    print("E_", parity, " = ", E, sep="")
    print("Normalization constant: ", norm, sep="")

    # Expectation values
    print("<x^2>: ", np.dot(psiN, x*x*psiN)*h, sep="")

    # Increment the parity for the next solution
    parity += 1

    # Where to start the next bracketing interval
    currentE = E2

    # Check that the tail of psiN is approximately zero
    tail = psiN[len(psiN)-5:]
    if np.dot(tail, tail) > 1e-3:
        print("\nWARNING! Your plotting limit is probably too large or too small for this "
              "wavefunction, so your results may not be accurate! At the ends of "
              "your plotting region, the wavefunction should be zero. If the "
              "wavefunction has not yet decayed to zero, your plotting limit is "
              "too small. If the wavefunction shoots to +/- infinity, your plotting"
              " limit is too large.")


# Plot the potential V(x) as well
xValues = np.append(-xValues[::-1], xValues[1:])
vValues = [V(i, case) for i in xValues]
plt.plot(xValues, vValues, label=r"$V(x)$", linestyle='dashed')

# Finish the plot
plt.legend(loc=1)
plt.xlabel(r"$x$")
plt.grid(True)
plt.ylim((-2, 2))
plt.show()
