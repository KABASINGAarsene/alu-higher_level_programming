#!/usr/bin/python3
"""
qwhduibyftvew fiwqugFBUYHASF
QWsfcqbyuasbvuiweqnfv qwIDJOQWFAS
wufgqbwjifknqwf qwf
qfqwfnjqnwfqwfq

"""

import json

def save_to_json_file(my_obj, filename):
    """
    jihgfueiwqghfeiwog wesahviowasv
    asvBASUVIJNWiaosjvwasv AC
    ASVCQasfcjkqSANVC QSAFC
    QSafcqadq

    """
    # Convert sets to lists for JSON serialization
    if isinstance(my_obj, set):
        my_obj = list(my_obj)

    # Attempt to write to the file
    with open(filename, "w") as file:
        json.dump(my_obj, file)
