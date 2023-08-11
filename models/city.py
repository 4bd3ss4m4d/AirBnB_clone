#!/usr/bin/python3

"""City Module"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attributes:
        state_id (str): State id
        name (str): City name

    Methods:
        __init__: Constructor of the City class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a City instance"""
        super().__init__(*args, **kwargs)
