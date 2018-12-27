#! /usr/bin/env python
"""
Defines a Rectangle class with two member variables length
and width. Various member functions, such as area and perimeter, are
defined, and the addition operator is overloaded to define rectangle addition.

Leon Hostetler, Mar. 30, 2017

USAGE: python rectangles.py
"""

from __future__ import division, print_function


class Rectangle:
    """Rectangle object declaration"""

    def __init__(self, length=1, width=1):
        """Initialize."""
        self.length = length
        self.width = width

    def area(self):
        """Compute and print the area of a rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Compute and print the perimeter of a rectangle."""
        return 2*self.length + 2*self.width

    def print(self):
        """Print the length, width, area, and circumference."""
        print("Length = ", self.length, sep="")
        print("Width = ", self.width, sep="")
        print("Area = ", self.area(), sep="")
        print("Perimeter = ", self.perimeter(), sep="")

    def __add__(self, other):
        """Define what it means to add two rectangles."""
        return Rectangle(self.length + other.length, self.width + other.width)


A = Rectangle(20, 10)
print("\nArea of first rectangle = ", A.area(), sep="")

B = Rectangle()
C = A + B

print("\nSecond Rectangle:")
C.print()
