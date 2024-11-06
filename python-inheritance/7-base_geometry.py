#!/usr/bin/python3

"""
wertyuikjhgfdxdrfvbnnnnnnm
dftgyujmjuytrewazxcfffvbnbvced
"""






class BaseGeometry:
    """
    A class for basic geometry operations
    """

    def area(self):
        """
        Raises an Exception for area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
