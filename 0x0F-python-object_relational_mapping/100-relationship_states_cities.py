#!/usr/bin/python3
""" Create relationship """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    sesion = sessionmaker(bind=engine)
    session = sesion()
    new_state = State(name='California')
    new_state.cities = [city(name='San Francisco')]
    session.add(new_state)
    session.commit()
