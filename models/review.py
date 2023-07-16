#!/usr/bin/python3
"""
This contains the Review class which inherits from the BaseModel class
and defines various attributes of a User.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    '''creating public class variables that
    define the Review Class '''

    place_id = ""
    user_id = ""
    text = ""
