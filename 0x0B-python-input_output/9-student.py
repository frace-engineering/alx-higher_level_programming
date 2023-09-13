#!/usr/bin/python3
"""Define a Student class"""


class Student:
    """Instantiate the variables"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        json_str = "{"
        for key, value in student_dict.items():
            if json_str != "{":
                json_str += ", "
            json_str += f'"{key}": "{value}"'
        json_str += "}"
        return json_str
