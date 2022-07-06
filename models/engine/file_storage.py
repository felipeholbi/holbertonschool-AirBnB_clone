#!/usr/bin/python3
""" class FileStorage """


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class FileStorage:
    """Define class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    classe = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
          "Place": Place, "Review": Review, "State": State, "User": User}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """saves a new object"""
        new_key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[new_key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json = dump(json_objects, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file-path, 'r') as file:
                j = json.load(file)
            for key in j:
                self.__objects[key] = classe[j[hey]["__class__"]](**j[key])
        except Exception:
            pass
