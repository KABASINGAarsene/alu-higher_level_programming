#!/usr/bin/python3
"""
the modeule is constituted by  a function that returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    This is the function that:
        - take an object in inpout.
        - returns the list of available attributes and methods of that object.
    """
    return dir(obj)
