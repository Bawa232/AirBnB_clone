#!/usr/bin/python3
"""
This contains the City class which inherits from the BaseModel class
and defines various attributes of a User.
"""


from models.base_model import BaseModel


class City(BaseModel):
    '''creating public class variables that
    define the City Class '''

    state_id = ""
    name = ""
