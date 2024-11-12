#!/usr/bin/python3
"""
Module to convert an object to a dictionary for JSON serialization.
"""

def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.
    """
    return obj.__dict__
