#!/usr/bin/python3
# Sangwani P Zyambo
""" Defines a function that writes a string
    to a text file (UTF8) and returns the number
    of characters written:
"""


def write_file(filename="", text=""):
    """ writes text to a file and return the number of chars written.
        param: (filename) - the file to write to.
        param: (text) - the string to be written to file.
    """
    with open(filename, 'w') as f:
        num_of_chars = 0
        for i in range(len(text)):
            f.write(text[i])
            num_of_chars += 1
    return num_of_chars
