#!/usr/bin/python3
""" this module is the command interpreter"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
