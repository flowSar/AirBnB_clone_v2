#!/usr/local/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=True)
    # cities = relationship('City', back_populates= 'State', cascade='all, delete-orphan')
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
