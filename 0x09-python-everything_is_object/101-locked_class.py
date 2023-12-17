#!/usr/bin/python3
"""A lockslass that prevents instanciation except name == "first_name" """


class LockedClass:
    """ Initialize an instance with name = first_name """
    def __init__(self, name="first_name"):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name_setter(self, value):
        """Conditionally crate an instance with name = first_name """
        if value == "first_name":
            self.name = value
        else:
            return
