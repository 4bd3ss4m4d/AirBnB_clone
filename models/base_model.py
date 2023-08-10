#!/usr/bin/python3

"""BaseModel class module"""

import models

from uuid import uuid4
from datetime import datetime

DATE_ISO8601_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class

    Attributes:
        id (str): unique id generated for the BaseModel instance
        created_at (datetime): datetime object representing the time the
        BaseModel instance was created
        updated_at (datetime): datetime object representing the time the
        BaseModel instance was updated

    Methods:
        __init__(*args, **kwargs): initializes a BaseModel instance
        __str__(): returns the string representation of the BaseModel instance
        save(): updates the updated_at attribute with the current datetime
        to_dict(): returns a dictionary containing all keys/values of the
        BaseModel instance
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance

        Args:
            *args: unused
            **kwargs: keyword arguments passed to the constructor

        Keyword Args:
            id (str): unique id generated for the BaseModel instance
            created_at (datetime): datetime object representing the time the
            BaseModel instance was created
            updated_at (datetime): datetime object representing the time the
            BaseModel instance was updated

        Returns:
            None
        """
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        kwargs[key], DATE_ISO8601_FORMAT))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            # Add a call to the new(self) method on storage
            models.storage.new(self)

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
        models.storage.save()  # Call the save() method of the storage instance

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
