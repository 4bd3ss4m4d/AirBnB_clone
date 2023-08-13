#!/usr/bin/python3

"""User class module"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class

    Attributes:
        email (str): email address of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user

    Methods:
        __init__(*args, **kwargs): initializes a User instance
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a User instance"""
        super().__init__(*args, **kwargs)
