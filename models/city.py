#!/usr/local/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60),
                      ForeignKey('states.id',
                                 ondelete='CASCADE'), nullable=True)
    name = Column(String(128), nullable=True)
    # state = relationship('State', back_populates='cities')
    state = relationship('State', back_populates='cities')
    places = relationship('Place', backref='cities',
                            cascade='all, delete, delete-orphan')
