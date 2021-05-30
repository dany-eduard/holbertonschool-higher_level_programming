#!/usr/bin/python3
""" Class definition """

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from relationship_state import Base


class City(Base):
    """ City class Args: Base(Object): Base class: """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
