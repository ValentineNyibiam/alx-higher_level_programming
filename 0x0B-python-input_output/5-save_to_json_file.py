#!/usr/bin/python3
""" This module defines a JSON file-writing function """
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - Writes an object to a text file,
    using a JSON representation
    Parameter:
    - my_obj: The obj to be written to file
    - filename: The file which object will be written to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
