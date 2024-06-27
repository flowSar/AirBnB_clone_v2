#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqllchemy import Column, String, ForeignKey
from sqllchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class represent states table in db
        Attributes:
            __tablename__ : database table
            name: state name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('') != 'db':
        from models import storage
        from city import City
        cities_list = []
        @property
        def cities(self):
            cities_instances = storage.all(City)
            for city in cities_instances.values():
                state_id = city['state_id']
                if state_id == State.id:
                    cities_list.append(city)
        return cities_list
    else:
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
