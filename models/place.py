#!/usr/bin/python3
"""
This contains the Place class which inherits from the BaseModel class
and defines various attributes of a User.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    '''creating public class variables that
    define the Place Class '''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
