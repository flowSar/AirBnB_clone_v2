#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os


class Amenity(BaseModel, Base):
    """amenity class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
