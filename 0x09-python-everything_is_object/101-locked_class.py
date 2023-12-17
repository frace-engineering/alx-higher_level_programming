#!/usr/bin/python3
class LockedClass:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name_setter(self, value):
        if value != "first_name"
            return
        else:
            self._name = vlue
