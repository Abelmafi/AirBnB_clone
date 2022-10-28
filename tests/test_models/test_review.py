#!/usr/bin/python3
"""..."""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.name = 'Review'
        self.value = Review

    def test_review_placeid(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.place_id), str)

    def test_review_userid(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.user_id), str)

    def test_review_text(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.text), str)

