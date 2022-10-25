#!/usr/bin/python3
"""Defining base model claiss"""
import uuid
from datetime import datetime


class BaseModel():
    """initilixing base model."""
    def __init__(self, name=None, my_number=0, id=None, created_at=None, updated_at=None):
        self.name = name
        self.my_number = my_number
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
                "name": self.name,
                "my_number": self.my_number,
                "id": self.id,
                "__class__": type(self).__name__,
                "created_at": self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
                }

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

