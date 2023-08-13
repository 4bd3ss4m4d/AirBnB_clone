#!/usr/bin/python3

"""
Contains the TestCityClasses classes
"""

from datetime import datetime
import os
import models
import unittest
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Tests for instantiating the City class"""

    def test_instantiates_with_no_args(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_name_is_public_class_attribute(self):
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_unique_ids_for_two_cities(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_different_created_at_for_two_cities(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_different_updated_at_for_two_cities(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_string_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        city = City()
        city.id = "abcdef"
        city.created_at = city.updated_at = dt
        city_str = city.__str__()
        self.assertIn("[City] (abcdef)", city_str)
        self.assertIn("'id': 'abcdef'", city_str)
        self.assertIn("'created_at': " + dt_repr, city_str)
        self.assertIn("'updated_at': " + dt_repr, city_str)

    def test_unused_args_not_in_dict(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_None_kwargs_raises_error(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCityToDict(unittest.TestCase):
    """Tests for converting City instance to dictionary"""

    def test_to_dict_returns_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_datetime_attributes_are_strs(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(str, type(city_dict["id"]))
        self.assertEqual(str, type(city_dict["created_at"]))
        self.assertEqual(str, type(city_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        city = City()
        city.id = "xyz123"
        city.created_at = city.updated_at = dt
        expected_dict = {
            'id': 'xyz123',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), expected_dict)

    def test_to_dict_differs_from_dunder_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_contains_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_contains_added_attributes(self):
        city = City()
        city.middle_name = "Metropolis"
        city.my_number = 98
        self.assertEqual("Metropolis", city.middle_name)
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_with_arg_raises_type_error(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


class TestCitySave(unittest.TestCase):
    """Tests for saving the City class"""

    def test_one_save_updates_updated_at(self):
        city = City()
        sleep(0.06)
        initial_updated_at = city.updated_at
        city.save()
        self.assertLess(initial_updated_at, city.updated_at)

    def test_multiple_saves_update_updated_at(self):
        city = City()
        sleep(0.06)
        initial_updated_at = city.updated_at
        city.save()
        updated_at_after_first_save = city.updated_at
        sleep(0.06)
        city.save()
        self.assertLess(updated_at_after_first_save, city.updated_at)

    def test_save_with_arg_raises_type_error(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    @classmethod
    def set_up_class(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tear_down_class(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_updates_file_content(self):
        city = City()
        city.save()
        city_id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


if __name__ == "__main__":
    unittest.main()
