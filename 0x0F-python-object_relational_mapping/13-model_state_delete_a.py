#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    sesion = sessionmaker(bind=engine)
    session = sesion()
    states = session.query(State).filter(State.name.contains('a')).all()
    for instance in states:
        session.delete(instance)
    session.commit()
    session.close()
