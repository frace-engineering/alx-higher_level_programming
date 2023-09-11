#!/usr/bin/python3
""" Define a class "is_same_class" that checks instance of class """


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class, else return false """
    if type(obj) is a_class:
        return True
    return False
