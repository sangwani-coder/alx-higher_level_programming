#!/usr/bin/python3
""" 
module contains function that adds
two integers a and b
"""

def add_integer(a, b=98):
    """adds 2 given  integers """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
