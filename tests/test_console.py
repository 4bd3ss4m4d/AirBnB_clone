#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
import json
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestConsoleClass(unittest.TestCase):
    """TestConsoleClass resume
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def set_up(self):
        """ sets up the initial conditions for the test"""
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tear_down(self):
        """ removes the test cases made"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
