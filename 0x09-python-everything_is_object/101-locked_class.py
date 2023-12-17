#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first name':
            super().__setattr__(name, value)
        else:
            raise AttributeErroe("Cant create the class")
    
