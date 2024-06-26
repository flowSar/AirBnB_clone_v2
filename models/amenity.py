#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Float, Column, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class is used to represent database table"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   back_populates="amenities")
