#!/usr/local/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Float, Column, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=True)
    name = Column(String(128), nullable=True)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=True, default=0)
    number_bathrooms = Column(Integer, nullable=True, default=0)
    max_guest = Column(Integer, nullable=True, default=0)
    price_by_night = Column(Integer, nullable=True, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    city = relationship('City', back_populates='places')
