#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref, mapped_column
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = mapped_column(String(128), nullable=False, sort_order=4)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = mapped_column(String(60), ForeignKey('states.id'),
                                 nullable=False, sort_order=5)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
