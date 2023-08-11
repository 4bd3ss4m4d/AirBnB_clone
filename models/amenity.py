#!/usr/bin/python3

"""Amenity Module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class

    Attributes:
        name (str): Amenity name

    Methods:
        __init__: Constructor of the Amenity class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity instance"""
        super().__init__(*args, **kwargs)
