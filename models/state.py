#!/usr/bin/python3

"""State Module"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class

    Attributes:
        name (str): State name

    Methods:
        __init__: Constructor of the State class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State instance"""
        super().__init__(*args, **kwargs)
