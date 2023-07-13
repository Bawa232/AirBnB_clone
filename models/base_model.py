#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self):
        ''' Constructor: initializes an instance of the class '''

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        ''' returns the str representation of the object '''

        ClsName = self.__class__.__name__
        return "[{}] ({}) {}".format(ClsName, self.id, self.__dict__)

    def save(self):
        ''' updates updated_at whenever an instance is modified '''

        self.updated_at = datetime.today()

    def to_dict(self):
        ''' returns the dictionary repr of an object '''

        new_dic = {}
        new_dic["__class__"] = self.__class__.__name__
        new_dic["created_at"] = created_at.isoformat()
        new_dic["updated_at"] = updated_at.isoformat()

        return new_dic
