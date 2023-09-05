#!/usr/bin/python3
"""Start link class to table in database 
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state class for use with sqlalchemy
        -> inherits from sqlalchemy declarative_base
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
