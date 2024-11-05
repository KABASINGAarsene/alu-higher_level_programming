#!/usr/bin/python3
"""
This is a module documentation.
"""


class Rectangle:
    """
    This is a class documentation.
    """
    # Class variable to keep track of the number of instances
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        # Increment the instance count whenever a new Rectangle is created
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        return "\n".join("#" * self.width for _ in range(self.height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
