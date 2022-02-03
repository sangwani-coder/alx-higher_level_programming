#!/usr/bin/python3
# Sangwani P Zyambo

""" Defines a function that append a string at
    the end of a text file(UTF8).
"""


def append_write(filename="", text=""):
    """ appends to a file if it exits
        otherwise create the file and write to it.
        And return the number of characters added.
    """
    with open(filename, 'a') as f:
        num_of_chars = 0
        for i in text:
            num_of_chars += 1
            f.write(i)
    return num_of_chars
