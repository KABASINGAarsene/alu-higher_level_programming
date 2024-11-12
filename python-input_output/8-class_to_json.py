#!/usr/bin/python3
"""
kjhgfdswertyuiokmnbvcxsqweiq
ytrewertyuiuytgfdsdfgh
iuytreedfgy
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__i_
