#!/usr/bin/python3
"""
QASDCFRTYUJMKBVCWQAPLuhvbeijdskvniusah
MKIUYTREWSZXAWERTFVBNMKwefw
QWERTYUIOLKJHGFDSXCVBNMwefwo
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")i
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    MNBVEDCJfihvy78nwq9SOFIV3HYFCVNMKOLIUYTREWQAZ4V29Q
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
        return f"[Rectangle] {self.__width}/{self.__height}"
