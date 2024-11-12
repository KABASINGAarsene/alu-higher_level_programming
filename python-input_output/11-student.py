#!/usr/bin/python3
"""
ashfgds asdghadsjhadsgd
dsg adsghadsjgh asdgjhasgdsxg
asgasgasgha AGUIagAGSKasgjdsgsg
"""


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
            Defaults to None.

        Returns:
            dict: A dictionary representation of the instance.
                  If attrs is a list of strings,
                  only specified attributes are included.
                  Otherwise, all attributes are included.
        """
        if attrs is not None and isinstance(attrs, list):
            result = {
                    attr: getattr(self, attr)
                    for attr in attrs
                    if hasattr(self, attr)
            }
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        instance with values from a dictionary.

        Args:
            json (dict): A dictionary where keys are
            attribute names and values are their new values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
