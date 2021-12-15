#!/usr/bin/python3
# Author: Sangwani P. Zyambo

"""
    Defines a function that prints a text with 2
    new lines after each of a specified character.
"""


def text_indentation(text):
    """
        Prints text with 2 new lines after each of
        these characters '.' '?' and ':'

        param: text(str) - the text to be searched for characters
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i not in '.?:':
            print(i, end='')
        else:
            print(i)
            print()
    print()
