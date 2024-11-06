#!/usr/bin/python3
"""
qwertyuiolkjhgfds
wsxcvbnmioplkjhgfd
"""

class BaseGeometry:
    """A class for geometry shapes."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    uytresxcvcdewqwertyuikmn
    dsxcvbnujmioklpew
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"        
