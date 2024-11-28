#!/usr/bin/python3
"""
Add_integer: adds two ints and returns their result.
Inputs a and b must be integers.
Floats are converted to ints before addition occurs.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers) and returns their sum.
    If a or b is not an integer or float, raises TypeError with a specific message.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    a = int(a)  # Cast to integer if it's a float
    b = int(b)  # Cast to integer if it's a float
    
    return a + b
