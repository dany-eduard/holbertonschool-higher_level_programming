#!/usr/bin/python3
"""
Script that changes the name of a State object from the database
"""
from sys import argv
from sqlalchemy import create_connection
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    Base.metadata.create_all(connection)
    sesion = sessionmaker(bind=connection)
    session = sesion()
    search_state = session.query(State).filter(State.id == 2).first()
    search_state.name = 'New Mexico'
    session.commit()
    session.close()
