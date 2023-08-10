#!/usr/bin/python3

"""BaseModel class module"""

from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self):
        """
        BaseModel class constructor

        Attributes:
            id (str): unique id of the BaseModel instance
            created_at (datetime): creation date of the BaseModel instance
            updated_at (datetime): update date of the BaseModel instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance"

        Returns:
            str: string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime

        Returns:
            None
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the BaseModel
        instance

        Returns:
            dict: dictionary containing all keys/values of the BaseModel
            instance
        """
        obj_dict = self.__dict__.copy()

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        return obj_dict
