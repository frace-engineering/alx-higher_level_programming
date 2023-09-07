#!/usr/bin/python3
def magic_string(ret="BestSchool"):
    for index, elem in enumerate(ret):
        print("{:s}, ".format((ret + ", ") * index))
