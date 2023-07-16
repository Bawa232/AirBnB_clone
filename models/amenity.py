#!/usr/bin/python3
"""
This contains the Amenity class which inherits from the BaseModel class
and defines various attributes of a User.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    '''creating public class variables that
    define the Amenity Class '''

    name = ""
