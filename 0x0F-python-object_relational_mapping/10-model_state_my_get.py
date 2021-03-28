#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(connection.format(
        username, password, db_name, pool_pre_pint=True))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (session.query(State).filter(State.name.like(argv[4])).first())
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
