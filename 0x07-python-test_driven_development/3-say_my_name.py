#!/usr/bin/python3
"""
A function that prints names
"""


def say_my_name(first_name, last_name=""):
    """Check if arguments are None, then throw TypeError"""
    if first_name is None and last_name is None:
        raise TypeError("say_my_name() missing 1 required"
                        " positional argument: 'first_name'")
    """Chech the data type, if not string, throw TypeError"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("{:s} {:s}".format(first_name, last_name))
