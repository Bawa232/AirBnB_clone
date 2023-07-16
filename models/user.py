#!/usr/bin/python3
"""
This contains the User class which inherits from the BaseModel class
and defines various attributes of a User.
"""

from models.base_model import BaseModel


class User(BaseModel):
    '''creating public class variables that
    define the User Class '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
