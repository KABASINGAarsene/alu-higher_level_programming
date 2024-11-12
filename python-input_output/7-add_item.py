#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""

import sys
from os import path

# Import the functions (shorter variable names)
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"   


# Load existing list from the file if it exists, otherwise initialize an empty list
if path.exists(filename):
    items = load_from_json(filename)
else:
    items = []

# Add command-line arguments to the list (skip the first argument)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json(items, filename)
