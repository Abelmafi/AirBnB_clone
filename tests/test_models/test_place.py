#!/usr/bin/python3
"""..."""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest


class test_Place(unittest.TestCase):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.name = 'Place'
        self.value = Place

    def test_place_cityid(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.city_id), str)

    def test_place_userid(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.user_id), str)

    def test_place_name(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.name), str)

    def test_place_description(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.description), str)

    def test_place_numberrooms(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.number_rooms), int)

    def test_place_numberBathRooms(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.number_bathrooms), int)

    def test_place_maxGuest(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.max_guest), int)

    def test_place_priceByNight(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.price_by_night), int)

    def test_place_latitude(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.latitude), float)

    def test_place_amenityIds(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.amenity_ids), list)
