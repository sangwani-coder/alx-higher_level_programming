#!/usr/bin/python3i
# Sangwani P Zyambo
""""
    Defines a function that returns an object(python data struct)
    represented by a JSON string.
"""


def from_json_string(my_obj):
    """ returns a python object from a JSON string"""
    import json

    return json.loads(my_obj)
