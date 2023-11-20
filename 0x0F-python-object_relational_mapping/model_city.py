#!/usr/bin/python3
""" python file that contains the class definition of a City
    and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sys import argv

Base = declarative_base()


class City(Base):
    """ State class inherites from Base """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(238), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
