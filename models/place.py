#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        amenity_ids = []
        from review import Review
        from models import storage
        reviews_list = []
        @property
        def reviews(self):
            """getter methode return list of reviews objects when
                Place.id == Review.place_id
            """
            reviews_objects = storage.all(Review)
            for re_object in reviews_objects:
                if Place.id == Review.place_id:
                    reviews_list.append(re_object)
            return reviews_list
