#!/usr/bin/python3
"""
class BaseModel
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """
    ...
    """
    def __init__(self, *args, **kwargs)
    """Initialize BaseModel class"""

    if kwargs:
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)
            if key in ('created_at', 'updated_at'):
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """
        ...
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                        self.__dict__)

    def save(self):
        """
        ...
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        ...
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['update_at'] = self.update_at.isoformat()
        return new_dict
