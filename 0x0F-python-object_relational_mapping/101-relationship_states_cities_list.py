#!/usr/bin/python3
""" Script that lists all states form database """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))
    sesion = sessionmaker(bind=engine)
    session = sesion()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
