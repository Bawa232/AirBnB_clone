#!/usr/bin/python3
"""This defines the base class which would be used by all other objects"""

from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel:
    """The base model which would be inherited by other classes

    This contains the `save` methodthat upates the instance, `to_dict`
    method which returns a dictionary representation of the instance

    Attributes:
        id(str): unique identifier of instance
        created_at(datetime class): time of instance creation
        updated_at(datetime class): last time instance was updated

    """

    def __init__(self, *args, **kwargs):
        """ Constructor: initializes an instance of the class

        Args:
            args(tuple): argument tuple which are not presently used
            kwargs(dict): a dictionary conatining attributes of the instance

        """

        date_form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, date_form)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        ''' returns the str representation of the object '''

        ClsName = self.__class__.__name__
        return "[{}] ({}) {}".format(ClsName, self.id, self.__dict__)

    def save(self):
        ''' updates updated_at whenever an instance is modified '''

        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        ''' returns the dictionary repr of an object '''

        new_dic = self.__dict__.copy()
        new_dic["__class__"] = self.__class__.__name__
        new_dic["created_at"] = self.created_at.isoformat()
        new_dic["updated_at"] = self.updated_at.isoformat()
        return new_dic
