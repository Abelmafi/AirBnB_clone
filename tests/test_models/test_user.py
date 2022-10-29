#!/usr/bin/python3
"""..."""
from models.base_model import BaseModel
from models.user import User
import unittest


class test_user(unittest.TestCase):
    """..."""
    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_user_email(self):
        cls = self.value()
        self.assertEqual(type(cls.email), str)

    def test_user_password(self):
        cls = self.value()
        self.assertEqual(type(cls.password), str)

    def test_user_firstName(self):
        cls = self.value()
        self.assertEqual(type(cls.first_name), str)

    def test_last_name(self):
        cls = self.value()
        self.assertEqual(type(cls.last_name), str)
