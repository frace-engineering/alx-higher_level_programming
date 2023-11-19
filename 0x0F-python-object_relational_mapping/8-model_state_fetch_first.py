#!/usr/bin/python3
"""
    Prints the first State object from the database hbtn_0e_6_usa
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

    first_state = session.query(State).order_by(State.id).first()
    if (first_state):
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
