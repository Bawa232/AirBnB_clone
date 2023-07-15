#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    '''creating public class variables that
    define the User Class '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
