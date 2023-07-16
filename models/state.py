#!/usr/bin/python#
"""
This contains the State class which inherits from the BaseModel class
and defines various attributes of a User.
"""


from models.base_model import BaseModel


class State(BaseModel):
    '''creating public class variables that
    define the State Class '''

    name = ""
