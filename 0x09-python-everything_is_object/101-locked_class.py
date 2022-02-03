#!/usr/bin/python3
""" Defines a locked class LockedClass"""


class LockedClass:
    """ Prevnts a user from dynamically creating new
        instance attributes, except if the new attribute is called
        first_name"""
    __slots__ = "first_name"
