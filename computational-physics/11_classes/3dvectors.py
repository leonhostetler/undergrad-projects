#! /usr/bin/env python
"""
Extends the Vector2D class to Vector3D using inheritance. For 3D
vectors, additional member functions, such as the cross product, are defined.

Leon Hostetler, Mar. 30, 2017

USAGE: python 3dvectors.py
"""

from __future__ import division, print_function
import numpy as np
import math as math


class Vector2D:
    """Vector2D Object declaration"""
    def __init__(self, aX=0.0, aY=0.0):
        self.setX(aX)
        self.setY(aY)

    def setX(self, aX):
        self.__iX = aX

    def setY(self, aY):
        self.__iY = aY

    def x(self):
        return self.__iX

    def y(self):
        return self.__iY

    def r(self):
        return math.sqrt(self.x()**2 + self.y()**2)

    def theta(self):
        return math.atan2(self.y(), self.x())

    def __add__(self, other):
        """ This returns the vector that is the sum of the given pair of vectors. """
        return Vector2D(self.x() + other.x(), self.y() + other.y())

    def __mul__(self, other):
        """ This returns the dot product of the pair of vectors. """
        return math.sqrt(self.x() * other.x() + self.y() * other.y())

    def print(self):
        """ Prints the vector. """
        print("vector(x, y) is (", self.x(), ", ", self.y(), ")", sep="")


class Vector3D(Vector2D):
    """Vector3D object declaration"""

    def __init__(self, aX, aY, aZ=0.0):
        self.setX(aX)
        self.setY(aY)
        self.setZ(aZ)

    def setZ(self, aZ):
        self.__iZ = aZ

    def z(self):
        return self.__iZ

    def mag(self):
        """ Return the magnitude of the vector. """
        return math.sqrt(self.x()**2 + self.y()**2 + self.z()**2)

    def cos_theta(self):
        """ Return the angle the vector makes with the positive z-axis. """
        return self.z()/self.mag()

    def phi(self):
        """ Return the angle the vector's projection into the xy-plane
        makes with the positive x-axis. """
        return math.atan2(self.y(), self.x())

    def __add__(self, other):
        """ Return the vector that is the sum of the given two vectors. """
        return Vector3D(self.x() + other.x(), self.y() + other.y(), self.z() + other.z())

    def __sub__(self, other):
        """ Vector subtraction. """
        return Vector3D(self.x() - other.x(), self.y() - other.y(), self.z() - other.z())

    def __mul__(self, other):
        """ Return the dot product of the two given vectors. """
        return self.x()*other.x() + self.y()*other.y() + self.z()*other.z()

    def __truediv__(self, other):
        """ Return the cross product of the two given vectors. """
        # Convert vectors to numpy format.
        vec1 = [self.x(), self.y(), self.z()]
        vec2 = [other.x(), other.y(), other.z()]

        # Perform numpy cross product
        cross = np.cross(vec1, vec2)

        return Vector3D(cross[0], cross[1], cross[2])

    def print(self):
        """ ** """
        print("vector(x, y, z) is (", self.x(), ", ", self.y(), ", ", self.z(), ")", sep="")


# Declare two vector objects from the Vector3D class
A = Vector3D(2, 3, 4)
B = Vector3D(3, 4, 5)

# Do stuff with the vector objects and print the results
print()
print("Vector A is:")
A.print()
print("Magnitude = ", A.mag(), sep="")
print("cos(theta) = ", A.cos_theta(), sep="")
print("phi = ", A.phi(), sep="")

print("\nVector B is:")
B.print()

print("\nThe dot product A*B is:")
print(A*B)

print("\nThe sum A + B is: ")
C = A + B
C.print()

print("\nThe difference B - A is: ")
D = B - A
D.print()

print("\nThe cross product A x B is: ")
E = A/B
E.print()
