#!/usr/bin/python3
"""This module provides the HBNBCommand class which provides
a command interpreter to be used in the AirBNB clone project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This is the command interpreter class for the AirBNB project
        which inherits from the cmd module.

    The Class implements various project specific commands and the usual
    `help` to get tips on usage and `quit` or `EOF` command to exit program

    """
    prompt = "(hbnb) "
    intro = "AirBNB Console 0.0.1"

    def do_quit(self, line):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, line):
        """Exits the command interpreter"""
        return True

    def emptyline(self):
        """Action to be taken if emptyline is passed"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
