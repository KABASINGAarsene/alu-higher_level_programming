#!/usr/bin/python3
"""
uhvbeijdskvertyujnbvcdwstyuioplmnbvcxsqFVB
YTREWASRTYUIOKJN
YTREWSXCVBNMKUFDERYU
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    fihmnbvcxswsdrftrewwertyuikmvbnmjuytrfvfyui
    """
    def __init__(self, width, height):
        # Validate width and height using integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Initialize width and height as private attributes
        self.__width = width
        self.__height = height
