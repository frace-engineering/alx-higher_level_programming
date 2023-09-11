#!/usr/bin/python3
"""
Function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """Return the list of the available attributes and methods """
    return [item for item in dir(obj)]
