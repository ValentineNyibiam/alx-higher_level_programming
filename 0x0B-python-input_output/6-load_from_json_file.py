#!/usr/bin/python3
""" This module defines a load from json file function """
import json
import os

def load_from_json_file(filename):
    """
    load_from_json_file - Creates an object from a JSON file
    Parameter:
    - filename: The file which object will be created from
    """
    if os.path.exists(filename):
        if os.stat(filename).st_size == 0:
            return []
    else:
        return []
    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        # when content of file is of invalid format
        return []
