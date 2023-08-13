#!/usr/bin/python3

"""Unit tests for models/engine/file_storage.py."""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Test instantiation of the FileStorage class."""

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initialization(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestFileStorageMethods(unittest.TestCase):
    """Test methods of the FileStorage class."""

    def set_up(self):
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    @classmethod
    def set_up_class(cls):
        cls.backup_file_path = models.storage._FileStorage__file_path
        models.storage._FileStorage__file_path = "test_file.json"

    @classmethod
    def tear_down_class(cls):
        os.remove("test_file.json")
        models.storage._FileStorage__file_path = cls.backup_file_path
    
    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base_model = BaseModel()
        some_user = User()
        some_state = State()
        some_place = Place()
        some_cit = City()
        some_amenity = Amenity()
        some_review = Review()
        models.storage.new(base_model)
        models.storage.new(some_user)
        models.storage.new(some_state)
        models.storage.new(some_place)
        models.storage.new(some_cit)
        models.storage.new(some_amenity)
        models.storage.new(some_review)
        models.storage.save()
        save_text = ""
        with open("test_file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + some_user.id, save_text)
            self.assertIn("State." + some_state.id, save_text)
            self.assertIn("Place." + some_place.id, save_text)
            self.assertIn("City." + some_cit.id, save_text)
            self.assertIn("Amenity." + some_amenity.id, save_text)
            self.assertIn("Review." + some_review.id, save_text)

    def test_new_obj(self):
        some_state = State()
        some_place = Place()
        some_city = City()
        some_amenity = Amenity()
        base_model = BaseModel()
        some_user = User()
        some_review = Review()
        models.storage.new(some_user)
        models.storage.new(some_state)
        models.storage.new(some_place)
        models.storage.new(some_city)
        models.storage.new(base_model)
        models.storage.new(some_amenity)
        models.storage.new(some_review)
        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())
        self.assertIn("User." + some_user.id, models.storage.all().keys())
        self.assertIn(some_user, models.storage.all().values())
        self.assertIn("State." + some_state.id, models.storage.all().keys())
        self.assertIn(some_state, models.storage.all().values())
        self.assertIn("Place." + some_place.id, models.storage.all().keys())
        self.assertIn(some_place, models.storage.all().values())
        self.assertIn("City." + some_city.id, models.storage.all().keys())
        self.assertIn(some_city, models.storage.all().values())
        self.assertIn("Amenity." + some_amenity.id,
                      models.storage.all().keys())
        self.assertIn(some_amenity, models.storage.all().values())
        self.assertIn("Review." + some_review.id,
                      models.storage.all().keys())
        self.assertIn(some_review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
    

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reloading(self):
        base_model = BaseModel()
        some_user = User()
        some_state = State()
        some_place = Place()
        some_city = City()
        some_amenity = Amenity()
        some_review = Review()
        models.storage.new(base_model)
        models.storage.new(some_user)
        models.storage.new(some_state)
        models.storage.new(some_place)
        models.storage.new(some_city)
        models.storage.new(some_amenity)
        models.storage.new(some_review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("User." + some_user.id, objs)
        self.assertIn("State." + some_state.id, objs)
        self.assertIn("Place." + some_place.id, objs)
        self.assertIn("City." + some_city.id, objs)
        self.assertIn("Amenity." + some_amenity.id, objs)
        self.assertIn("Review." + some_review.id, objs)

    def test_reloading_with_no_file(self):
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
