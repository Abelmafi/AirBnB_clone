#!/usr/bin/python3
"""..."""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_amenity(unittest.TestCase):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.name = 'Amenity'
        self.value = Amenity

    def test_amenity(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.name), str)
