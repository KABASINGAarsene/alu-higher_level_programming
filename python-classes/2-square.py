#!/usr/bin/python3


"""
This code create an empty class.
"""


class Square:
    """
    This is an empty class
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except Exception as e:
            raise e
