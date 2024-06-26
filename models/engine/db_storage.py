#!/usr/bin/python3
"""
    this module to deling with mysql database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """
        in this class where we're goign to set connection to db
        and load and insert and delete and averything that related
        to dealing with our database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
            in this unit function wheen going to get env variable
            that was needed for connecting to db like user host and
            password
        """
        from models.base_model import Base
        user = os.getenv('HBNB_MYSQL_USER')
        passwrd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwrd,
                                              host, db_name),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.drop_all(self.__engine)

    def all(self, cls=None):
        """lod from db all object or specific object depend on cls"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        class_names = [User, State, City, Amenity, Place, Review]
        objects = {}
        if cls:
            instance = self.__session.query(cls.__name__).all()
            return {f'{cls.__name__}.{instance.id}': instance}
        for class_name in class_names:
            try:
                instance = self.__session.query(class_name).all()
                objects[f'{class_name.__name__}.{instance.id}'] = instance
            except Exception as e:
                pass

        return objects

    def new(self, obj):
        """add new object to db"""
        self.reload()
        self.__session.add(obj)

    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from db if it was found"""
        if obj:
            obj_to_delete = self.__session.query(obj).all()
            if obj_to_delete:
                self.__session.delete(obj_to_delete)
                self.__session.commit()

    def reload(self):
        """create db tables and add session"""
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
        self.__session.commit()
