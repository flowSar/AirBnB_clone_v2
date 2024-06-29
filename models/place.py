#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
import os
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


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
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', backref='place_amenities',
                                 secondary='place_amenity',
                                 viewonly=False)
    else:
        amenity_ids = []
        reviews_list = []

        @property
        def reviews(self):
            """getter methode return list of reviews objects when
                Place.id == Review.place_id
            """
            from models.review import Review
            import models
            reviews_objects = models.storage.all(Review)
            for re_object in reviews_objects:
                if Place.id == Review.place_id:
                    reviews_list.append(re_object)
            return reviews_list

        @property
        def amenities(self):
            """getter method return list of amenity instnce based on
               amenity_ids
            """
            import models
            Amenity_list = []
            for instance in models.storage.all(Amenity):
                for am_id in self.amenity_ids:
                    if am_id == instance.id:
                        Amenity_list.append(instance)
            return Amenity_list

        @amenities.setter
        def Amenity(self, obj):
            """setter method for amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
