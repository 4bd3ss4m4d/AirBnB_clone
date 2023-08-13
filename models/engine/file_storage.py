#!/usr/bin/python3

"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects

        Returns:
            dict: __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): object to be set in __objects

        Returns:
            None
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)

        Returns:
            None
        """
        objects_dict = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects

        Returns:
            None
        """
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = value["__class__"]
                    self.__objects[key] = eval(class_name + "(**value)")
        except FileNotFoundError:
            pass
