#!/usr/bin/python3
"""..."""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_city(unittest.TestCase):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.name = 'City'
        self.value = City

    def test_city_name(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.name), str)

    def test_city_id(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.state_id), str) 
