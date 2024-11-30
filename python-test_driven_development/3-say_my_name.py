#!/usr/bin/python3
"""
This module writes a function that prints the first and last names
"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>"""
    if not isinstance((first_name), str):
        raise TypeError("first_name must be a string")
    if not isinstance((last_name), str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
