#!/usr/bin/python3
"""
This is the module documentation. The module create a class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (same for width and height).
            x (int): The x-coordinate (default: 0).
            y (int): The y-coordinate (default: 0).
            id (int): An optional ID for the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Get the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes of the square.
        Args:
            *args: Non-keyword arguments assigned in order:
                1st -> id
                2nd -> size
                3rd -> x
                4th -> y
            **kwargs: Key-value pairs for attributes to update.
                Ignored if *args exists and is not empty.
        """
        # Handle *args if present
        if args:
            attributes = ['id', 'size', 'x', 'y']
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
        Return the dictionary representation of the Square.
        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
