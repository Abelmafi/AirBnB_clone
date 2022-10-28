#!/usr/bin/python3
"""..."""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest


class test_state(unittest.TestCase):
    """..."""

    def __init__(self, *args, **kwargs):
        """..."""
        super().__init__(*args, **kwargs)
        self.name = 'State'
        self.value = State

    def test_state_name(self):
        """..."""
        cls = self.value()
        self.assertEqual(type(cls.name), str)
