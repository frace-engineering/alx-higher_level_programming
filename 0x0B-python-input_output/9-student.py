#!/usr/bin/python3
"""Define a Student class"""


class Student:
    """Instantiate the variables"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
        """
        student_dict = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
        return student_dict
        """
