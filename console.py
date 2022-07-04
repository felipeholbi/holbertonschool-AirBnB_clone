#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = '(hbnb)'

if __name__ == '__main__':
    HBNBCommand().cmdloop()
