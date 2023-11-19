#!/usr/bin/python3
""" python file that contains the class definition of a State
    and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sys import argv

Base = declarative_base()


class State(Base):
    """ State class inherites from Base """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(238), nullable=False)
