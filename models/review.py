#!/usr/bin/python3

"""Review Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    Attributes:
        place_id (str): Place id
        user_id (str): User id
        text (str): Review text

    Methods:
        __init__: Constructor of the Review class
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance"""
        super().__init__(*args, **kwargs)
