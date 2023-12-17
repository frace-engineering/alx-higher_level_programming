#!/usr/bin/python3
"""A lockslass that prevents instanciation except name == "first_name" """


class LockedClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name_setter(self, value):
        if value == "first_name":
            self.name = value
        else:
            return
