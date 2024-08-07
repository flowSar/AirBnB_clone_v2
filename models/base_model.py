#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.orm import mapped_column
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = mapped_column(String(60), nullable=False,
                       primary_key=True, sort_order=1)
    created_at = mapped_column(DateTime, nullable=False,
                               default=datetime.utcnow, sort_order=2)
    updated_at = mapped_column(DateTime, nullable=False,
                               default=datetime.utcnow, sort_order=3)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'updated_at' in kwargs and 'created_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs['__class__']
                self.__dict__.update(kwargs)
            else:
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        storage.new(self)
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if 'created_at' in dictionary and 'updated_at' in dictionary:
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
        found = False
        for key in dictionary:
            if key == '_sa_instance_state':
                found = True
        if found:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """calling for a delete methode from storage
        to delete current instance"""
        from models import storage
        storage.delete(self)
