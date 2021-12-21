#!/usr/bin/python3
# Sangwani P Zyambo

""" This module defines a function that reads a text
    file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """ Read a UTF8 text file and
        print it to stdout.
        param: filename - the file to open and read.
    """
    with open(filename) as f:
        text = f.read()
        for t in text:
            print(t, end='')
