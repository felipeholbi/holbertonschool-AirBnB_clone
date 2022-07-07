#!/usr/bin/python3
""" class BaseModel """

import models
import uuid
from datetime import datetime

date_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    this is the superclasse
    """
    def __init__(self, *args, **kwargs):
        """ Initialize BaseModel class """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, date_time)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, date_time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ Updates the public instance attribute """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        for key, value in new_dict.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
        return new_dict

    def __str__(self):
        """ Returns a string BaseModel class """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
