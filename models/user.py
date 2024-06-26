#!/usr/local/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=True)
        password = Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
