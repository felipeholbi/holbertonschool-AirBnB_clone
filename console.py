#!/usr/bin/python3
""" this module is the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

classe = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
          "Place": Place, "Review": Review, "State": State, "User": User}

class HBNBCommand(cmd.Cmd):
    """develop methods"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF: to exit the program"""
        return True

    def do_quit(self, line):
        """quit: to exit the program"""
        return True

    def emptyline(self):
        """any action"""
        pass

    def main():
        """Don't executed when imported"""
        pass

    def do_create(self, line):
        new_instance = BaseModel(None, line)
        print(f"{new_instance}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
