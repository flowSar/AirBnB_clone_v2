#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os
from models.city import City


class State(BaseModel, Base):
    """ State class represent states table in db
        Attributes:
            __tablename__ : database table
            name: state name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''
        @property
        def cities(self):
            from models import storage
            cities_list = []
            cities_instances = storage.all(City)
            for city in cities_instances.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
