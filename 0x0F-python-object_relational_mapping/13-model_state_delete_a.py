#!/usr/bin/python3
"""
    deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    DB_URL = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(DB_URL, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if 'a' in state.name:
            session.delete(state)

    session.commit()
    session.close()
