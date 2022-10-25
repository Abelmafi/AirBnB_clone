#!/usr/bin/python3
"""Defining base model claiss"""
import uuid
from datetime import datetime


class BaseModel():
    """initilixing base model."""
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """saves """
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
                "name": self.name,
                "my_number": self.my_number,
                "id": self.id,
                "__class__": type(self).__name__,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                }

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

