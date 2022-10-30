#!/usr/bin/python3
"""..."""
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

#"""
#This module is the unittest file for the class: State.
#"""
#from genericpath import exists
#import unittest
#from models.state import State
#from models.engine.file_storage import FileStorage
##import pep8
#from models import storage
#
#
#class TestBaseClass(unittest.TestCase):
#    """
#    This class is for testing State.
#    """
#    def setUp(self):
#        """
#        Setup method.
#        """
#        self.State1 = State()
#        self.State2 = State()
#        State3_dict = self.State1.to_dict()
#        self.State3 = State(**State3_dict)
#
#    def tearDown(self):
#        """
#        Teardown method.
#        """
#        del self.State1
#        del self.State2
#        del self.State3
#        storage.save()
#
##    def test_pep8(self):
##        """
##        Testing pep8 compliance.
##        """
##        pep8style = pep8.StyleGuide(quiet=True)
##        result = pep8style.check_files(['models/base_model.py'])
##        self.assertEqual(result.total_errors, 0,
##                         "Found code style errors (and warnings).")
##
#    def test_documentation(self):
#        """
#        tests for module, class, & method documentation.
#        """
#        # Class docstring
#        self.assertTrue(len(State.__doc__) >= 1)
#
#    def test_init(self):
#        """
#        Tests the init method.
#        """
#        self.assertEqual(self.State1.name, "")
#
#if __name__ == "__main__":
#    unittest.main()
