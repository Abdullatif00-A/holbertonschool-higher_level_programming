#!/usr/bin/python3
"""File that contains the contains the class definition of a City"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
