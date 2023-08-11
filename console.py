#!/usr/bin/python3

"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB Clone project

    Attributes:
        prompt (str): The command prompt
        __clase_names (dict): The available classes

    Methods:
        do_quit: Quit command to exit the program
        do_EOF: EOF command to exit the program when the user inputs EOF
                (Ctrl+D)
        emptyline: Called when an empty line is entered in response to
                   the prompt
        do_create: Creates a new instance of BaseModel, saves it (to the
                   JSON file) and prints the id
        do_show: Prints the string representation of an instance based
                 on the class name and id
        do_destroy: Deletes an instance based on the class name and id
                    (save the change into the JSON file)
        do_all: Prints all string representation of all instances based
                or not on the class name
        do_update: Updates an instance based on the class name and id by
                   adding or updating attribute (save the change into the
                   JSON file)
    """

    prompt = "(hbnb) "
    __clase_names = {
        "BaseModel",
        "User",
    }

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id

        Usage: create <class name>

        Args:
            arg (str): class name of the instance to create

        Return:
            None
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__clase_names:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id

        Usage: show <class name> <id>

        Args:
            arg (str): class name and id of the instance to show

        Return:
            None
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__clase_names:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file)

        Usage: destroy <class name> <id>

        Args:
            arg (str): class name and id of the instance to destroy

        Return:
            None
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__clase_names:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name

        Usage: all <class name> or all

        Args:
            arg (str): class name of the instance to show or nothing

        Return:
            None
        """
        if not arg:
            objects = storage.all()
            print([str(obj) for obj in objects.values()])
        elif arg not in HBNBCommand.__clase_names:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            print([str(obj) for obj in objects.values() if
                   type(obj).__name__ == arg])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Args:
            arg (str): class name, id, attribute name and attribute value of
            the instance to update

        Return:
            None
        """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.__clase_names:
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif len(arg.split()) == 2:
            print("** attribute name missing **")
        elif len(arg.split()) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg.split()[0], arg.split()[1])
            if key in storage.all():
                setattr(storage.all()[key], arg.split()[2], arg.split()[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
