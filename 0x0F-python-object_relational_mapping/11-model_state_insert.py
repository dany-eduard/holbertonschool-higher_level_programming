#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(connection.format(
        username, password, db_name, pool_pre_pint=True))
    sesion = sessionmaker(bind=engine)
    session = sesion()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
