#!/usr/bin/python3

"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
from models import state
from models.base_model import BaseModel
import unittest

STATE = state.State


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""
    @classmethod
    def set_up_class(cls):
        """Set up for the doc tests"""
        cls.state_functions = inspect.getmembers(STATE, inspect.isfunction)

    def test_module_docstring(self):
        """Test for the state.py module docstring"""
        self.assertIsNot(state.__doc__, None,
                         "state.py needs a docstring")
        self.assertTrue(len(state.__doc__) >= 1,
                        "state.py needs a docstring")

    def test_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(STATE.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(STATE.__doc__) >= 1,
                        "State class needs a docstring")

    def test_method_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for func_name, func in self.state_functions:
            self.assertIsNot(func.__doc__, None,
                             "{:s} method needs a docstring".format(func_name))
            self.assertTrue(len(func.__doc__) >= 1,
                            "{:s} method needs a docstring".format(func_name))


class TestStateFunctionality(unittest.TestCase):
    """Test the functionality of the State class"""
    def test_subclass_of_BaseModel(self):
        """Test that State is a subclass of BaseModel"""
        state_instance = STATE()
        self.assertIsInstance(state_instance, BaseModel)
        self.assertTrue(hasattr(state_instance, "id"))
        self.assertTrue(hasattr(state_instance, "created_at"))
        self.assertTrue(hasattr(state_instance, "updated_at"))

    def test_name_attribute(self):
        """Test that State has attribute 'name', and it's initialized as an empty string"""
        state_instance = STATE()
        self.assertTrue(hasattr(state_instance, "name"))
        self.assertEqual(state_instance.name, "")

    def test_to_dict_creates_dictionary(self):
        """Test that the to_dict method creates a dictionary with proper attributes"""
        s = STATE()
        new_dict = s.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in s.__dict__:
            self.assertTrue(attr in new_dict)
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """Test that the values in the dictionary returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = STATE()
        new_dict = s.to_dict()
        self.assertEqual(new_dict["__class__"], "State")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], s.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], s.updated_at.strftime(time_format))

    def test_string_representation(self):
        """Test that the str method provides the correct output"""
        state_instance = STATE()
        expected_string = "[State] ({}) {}".format(state_instance.id, state_instance.__dict__)
        self.assertEqual(expected_string, str(state_instance))


if __name__ == "__main__":
    unittest.main()