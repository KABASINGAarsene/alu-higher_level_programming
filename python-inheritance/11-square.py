#!/usr/bin/python3
"""
This module defines geometric shapes with basic validation, including:
   - A `BaseGeometry` class that provides validation methods.
   - A `Rectangle` class that inherits from `BaseGeometry` and calculates area.
   - A `Square` class that inherits from `Rectangle` and represents a square.
"""


class BaseGeometry:
    """
    A `BaseGeometry` class that provides validation methods.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        # Validate width and height using integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Initialize width and height as private attributes
        self.__width = width
        self.__height = height

    def area(self):
        # Returns the area of the rectangle
        return self.__width * self.__height

    def __str__(self):
        # String representation of the rectangle
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """
    def __init__(self, size):
        # Validate size and initialize it as a private attribute
        self.integer_validator("size", size)
        self.__size = size
        # Call the superclass's __init__ with size for both width and height
        super().__init__(size, size)

    def area(self):
        # Returns the area of the square
        return self.__size ** 2

    def __str__(self):
        # String representation of the square
        return f"[Square] {self.__size}/{self.__size}"
