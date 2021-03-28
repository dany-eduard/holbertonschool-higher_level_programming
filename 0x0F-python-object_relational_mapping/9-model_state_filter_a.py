#!/usr/bin/python3
"""
Prints the first State object from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    engine = create_engine(connection.format(
        username, password, db_name, pool_pre_pint=True))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(
        State.name. ilike("%a%")).order_by(State.id).all()

    for item in query:
        print("{}: {}".format(item.id, item.name))
