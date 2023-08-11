#!/usr/bin/python3

"""Console module"""

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program

        Usage: quit

        Return:
            True
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program when the user inputs EOF (Ctrl+D)

        Usage: EOF or CTRL+D

        Return:
            True
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
