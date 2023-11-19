#!/usr/bin/python3
""" 
    lists all State objects that contain the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
DB_URL = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"


if __name__ == "__main__":
    engine = create_engine(DB_URL, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print(f"{state.id}: {state.name}")
