#!/usr/bin/python3
"""The class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle shape.
    Inherits from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.
        Args:
           width(int): The width of the rectangle.
           height (int): The height of the rectangle.
           x (int): The horizontal position of the rectangle.
           y (int): The vertical position of the rectangle.
           id (int): The ID of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """"Get the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """get the horizontal position of the rectangle."""
        return self.__x

    @property
    def y(self):
        """get the vertical position of the rectangle."""
        return self.__y

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args:
            value (int): The height value to set.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Set the width t of the rectangle.
        Args:
            value (int): The width value to set.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.

        Args:
        value (int): The x-coordinate value to set.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """"Calculate the area of  the rectangle
        Returns:
               int: the area value"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character '#'
           considering position x and y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return the string representation of the Rectangle instance."""
        sides = (
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
                )
        res = '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(
                sides[0], sides[1], sides[2], sides[3], sides[4]
                )
        return res

    def update(self, *args, **kwargs):
        """Updates the attributes of this rectangle.
        Args:
            args (tuple): A tuple of non-keyword arguments.
            kwargs (dict): A dictionary of keyword arguments.
        """
        attrs = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary representation of this rectangle.
        Returns:
            dict: A dictionary representation of this rectangle.
        """
        res = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return res
