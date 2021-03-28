#!/usr/bin/python3
''' Script that lists all states form database '''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))

    sesion = sessionmaker(bind=engine)
    session = sesion()
    cities = session.query(State, City).\
        filter(State.id == City.state_id)
    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()
    session.close()
