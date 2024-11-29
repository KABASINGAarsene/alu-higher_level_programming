#!/usr/bin/python3
"""
This is the module documentation. The module create a class Base
"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate (default: 0).
            y (int): The y-coordinate (default: 0).
            id (int): An optional ID for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Width attribute
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Height attribute
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # X attribute
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Y attribute
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Print the rectangle using the `#` character.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        str = (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
               f"{self.width}/{self.height}")
        return str

    def update(self, *args, **kwargs):
        """
        Update attributes of the rectangle.
        Args:
            *args: Non-keyword arguments assigned in order:
                1st -> id
                2nd -> width
                3rd -> height
                4th -> x
                5th -> y
            **kwargs: Key-value pairs for attributes to update.
                Ignored if *args exists and is not empty.
        """
        # Handle *args if present
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        # Handle **kwargs if *args is empty
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle.
        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
