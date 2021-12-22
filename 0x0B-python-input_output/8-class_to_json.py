#!/usr/bin/python3
# Sangwani P Zyambo

"""defines a function that returns the dictionary
    description
"""


def class_to_json(obj):
    """returns a dictionary decription of a simple data structure"""
    return obj.__dict__
