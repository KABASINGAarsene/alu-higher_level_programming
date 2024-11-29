#!/usr/bin/python3
"""
This module adds two integers
"""


def add_integer(a, b=98):
    """Write a function that adds 2 integers."""
    # Validate that a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Validate that b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a + 1 == a or b + 1 == b:
        raise OverflowError("number too large")

    # Cast a and b to integers and return their sum
    return int(a) + int(b)
