#!/usr/bin/python3
"""
    Change the name of a State object from the database hbtn_0e_6_usa
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

    result = session.query(State).filter(State.id == 2).first()
    if result:
        result.name = "New Mexico"

    session.commit()
    session.close()
