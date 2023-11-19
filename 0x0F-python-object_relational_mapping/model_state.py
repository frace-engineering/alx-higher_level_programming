#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence, create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

""" python file that contains the class definition of a State
    and an instance Base = declarative_base()
"""
DATABASE_URL = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(238), nullable=False)


if __name__ == "__main__":
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    Base.metadata.create_all(engine)
