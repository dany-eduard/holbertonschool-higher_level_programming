#!/usr/bin/python3
"""
Prints the first Sate object from the database
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
    item = session.query(State).first()
    if item is None:
        print("Nothing")
    else:
        print("{}: {}".format(item.id, item.name))
