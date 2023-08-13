#!/usr/bin/python3

"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex


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
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
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

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class

        Usage: <class name>.count()

        Args:
            arg (str): class name of the instance to count
        """
        objects_dict = storage.all()
        count = sum(1 for key in objects_dict if arg in key)
        print(count)

    def do_update_using_class(self, arg):
        if not arg:
            print("** class name missing **")
            return
        my_dict = "{" + arg.split("{")[1]
        data = shlex.split(arg)
        storage.reload()
        obj = storage.all()
        if data[0] not in self.__clase_names.keys():
            print("** class doesn't exist **")
            return
        if (len(data) == 1):
            print("** instance id missing **")
            return
        try:
            key = data[0] + "." + data[1]
            obj[key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dict == "{"):
            print("** attribute name missing **")
            return

        my_dict = my_dict.replace("\'", "\"")
        my_dict = json.loads(my_dict)
        my_instance = obj[key]
        for my_key in my_dict:
            if hasattr(my_instance, my_key):
                data_type = type(getattr(my_instance, my_key))
                setattr(my_instance, my_key, my_dict[my_key])
            else:
                setattr(my_instance, my_key, my_dict[my_key])
        storage.save()

    def default(self, arg):
        """
        Called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and
        returns.
        """
        methods_dict = {
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "all": self.do_all,
            "update": self.do_update
        }
        
        commands = arg.strip().split(".")
        if len(commands) != 2:
            return cmd.Cmd.default(self, arg)
        
        class_name = commands[0]
        command = commands[1].split("(")[0]
        line = ""
        if (command == "update" and commands[1].split("(")[1][-2] == "}"):
            inputs = commands[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = commands[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in methods_dict.keys()):
            methods_dict[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
