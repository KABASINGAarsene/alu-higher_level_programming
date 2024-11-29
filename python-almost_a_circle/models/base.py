#!/usr/bin/python3
"""
This is the module documentation. The module create a class Base
"""

import json
import os


class Base:
    """Base class for managing IDs."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        Args:
            id (int): An optional ID for the instance. If not provided,
            an ID is automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: JSON string representation of list_dictionaries
            or "[]" if None or empty.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = f"{cls.__name__}.json"  # File name based on class name
        list_dicts = []

        if list_objs is not None:
            """Convert each object in list_objs
            to a dictionary using to_dictionary()"""
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert list of dictionaries to JSON string
        json_string = cls.to_json_string(list_dicts)

        # Write JSON string to the file
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string json_string.
        Args:
            json_string (str): A JSON string representing a listofdictionaries
        Returns:
            list: A list of dictionaries represented by json_string,
            or an empty list if None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance of the class with attributes setBasedOnDictionary.
        Args:
            **dictionary: A dictionary of attributes to set on the instance.
        Returns:
            An instance of cls with attributes updated.
        """
        # Create a "dummy" instance
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Rectangle requires width and height
        elif cls.__name__ == "Square":
            dummy = cls(1)     # Square requires size
        else:
            raise ValueError(f"Unsupported class: {cls.__name__}")

        # Update the dummy instance with the real attributes
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.
        """
        filename = f"{cls.__name__}.json"

        # Check if file exists
        if not os.path.exists(filename):
            return []

        # Read the file content
        with open(filename, "r") as file:
            json_string = file.read()

        # Deserialize JSON string into a list of dictionaries
        list_dicts = cls.from_json_string(json_string)

        # Create and return a list of instances using the dictionaries
        instances = [cls.create(**d) for d in list_dicts]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects to a CSV file.
        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        filename = f"{cls.__name__}.csv"
        if list_objs is None or len(list_objs) == 0:
            list_objs = []

        # Field names for CSV based on the object type
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]

        # Write to CSV file
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # Write header
            for obj in list_objs:
                # Write object data as a row
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a list of objects from a CSV file.
        Returns:
            list: List of instances loaded from the CSV file.
        """
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        # Field names for CSV based on the object type
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]

        # Read from CSV file
        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            list_dicts = [
                dict((k, int(v)) for k, v in row.items())
                for row in reader
            ]

        # Convert dictionaries to instances
        return [cls.create(**d) for d in list_dicts]
