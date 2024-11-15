#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    # Convert sets to lists for JSON serialization
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    # Attempt to write to the file
    with open(filename, "w") as file:
        json.dump(my_obj, file)
