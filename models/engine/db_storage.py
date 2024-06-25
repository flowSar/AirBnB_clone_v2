#!/usr/local/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    __engine = None
    __session = None
    
    def __init__(self):
        from models.base_model import Base
        user = os.getenv('HBNB_MYSQL_USER')
        passwrd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, passwrd, host, db_name), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.drop_all(self.__engine)
        
    def all(self, cls=None):
        class_names = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
        objects = {}
        if cls:
            instance = self.__session.query(cls.__name__).all()
            return {f'{cls.__name__}.{instance.id}': instance}
        for class_name in class_names:
            instance = self.__session.query(class_name).all()
            objects[f'{class_name}.{instance.id}'] = instance
        return objects
    
    def new(self, obj):
        self.__session.add(obj)
    
    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj:
            obj_to_delete = self.__session.query(obj).all()
            if obj_to_delete:
                self.__session.delete(obj_to_delete)
                self.__session.commit()
    
    def reload(self):
        from models.base_model import Base
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
            
        
