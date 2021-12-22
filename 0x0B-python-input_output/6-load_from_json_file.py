#!/usr/bin/python3
# Sangwani P Zyambo
""" This module defines a function that creates a python object
    from a JSON file.
"""


def load_from_json_file(filename):
    """Creates a python Object from a JSON file"""
    import json
    with open(filename) as f:
        return json.load(f)
