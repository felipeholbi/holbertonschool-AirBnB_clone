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
    prompt = '(hbnb) '


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
        if line == "" or line is None:
            print("** class name missing **")
        elif line in classe.keys():
            '''print("** eureka **")'''
            new_instance = classe[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")



    def do_show(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in HBNBCommand.classe:
            print("** class doesn't exist **")
    
    def do_destroy(self, line):
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in HBNBCommand.classe:
            print("** class doesn't exist **")
    
    def do_all(self, line):
        if line not in HBNBCommand.classe:
            print("** class doesn't exist **")
    




if __name__ == '__main__':
    HBNBCommand().cmdloop()
