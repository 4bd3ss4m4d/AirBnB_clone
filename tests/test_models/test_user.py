#!/usr/bin/python3

"""Defines unittests for models/user.py."""

import unittest
from datetime import datetime
from time import sleep
import os
import models
from models.user import User


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_instantiates_without_arguments(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_string(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_string(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_string(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_string(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_string(self):
        self.assertEqual(str, type(User.last_name))

    def test_unique_ids_for_different_users(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_different_created_at_for_users(self):
        user1 = User()
        sleep(0.06)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_different_updated_at_for_users(self):
        user1 = User()
        sleep(0.06)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user = User()
        user.id = "abcdef"
        user.created_at = user.updated_at = dt
        user_str = user.__str__()
        self.assertIn("[User] (abcdef)", user_str)
        self.assertIn("'id': 'abcdef'", user_str)
        self.assertIn("'created_at': " + dt_repr, user_str)
        self.assertIn("'updated_at': " + dt_repr, user_str)

    def test_unused_args_not_in_dict(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="xyz", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "xyz")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)

    def test_instantiation_with_None_kwargs_raises_error(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def set_up_class(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tear_down_class(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_updates_updated_at(self):
        user = User()
        sleep(0.05)
        initial_updated_at = user.updated_at
        user.save()
        self.assertLess(initial_updated_at, user.updated_at)

    def test_multiple_saves_updates_updated_at(self):
        user = User()
        sleep(0.05)
        initial_updated_at = user.updated_at
        user.save()
        updated_at_after_first_save = user.updated_at
        sleep(0.05)
        user.save()
        self.assertLess(updated_at_after_first_save, user.updated_at)

    def test_save_with_arg_raises_type_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file_content(self):
        user = User()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(user_id, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_returns_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Middle"
        user.my_number = 98
        self.assertEqual("Middle", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_datetime_attributes_are_strs_in_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        user = User()
        user.id = "xyz123"
        user.created_at = user.updated_at = dt
        expected_dict = {
            'id': 'xyz123',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), expected_dict)

    def test_to_dict_differs_from_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg_raises_type_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()