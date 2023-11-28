#!/usr/bin/python3
"""contains the class definition of a State and an instance"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
