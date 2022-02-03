#!/usr/bin/python3
# Sangwani P Zyambo
""" Defines a funtion that writes an Object to a text file,
    using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """ writes a python object to a text file,
        using JSON representation
        param: (my_obj) - the object to be converted to json
        param: (filename) - the file to write my_obj to.
    """
    import json

    with open(filename, 'w') as f:
            json.dump(my_obj, f)
