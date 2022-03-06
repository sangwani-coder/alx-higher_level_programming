#!/usr/bin/python3
"""
    defines a state class and an instance Base = declarative_base():
    state clas:
        inherits from Base
        links to the MYSQL tables states
        class attribute id that represents a column of an auto-generated
        unique integer, can't be null.
        class attribute name that represents a column of a string with
        maximum 128 characters and can't be null.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
