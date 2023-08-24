#!/usr/bin/python3
"""Python console prints prompt and quits"""

import cmd
from datetime import datetime
import models
import re


class HBNBCommand(cmd.Cmd):
    """Command console class"""
    prompt = '(hbnb) '

    def precmd(self, line):
        return line.strip()

    def do_EOF(self, line):
        """
        EOF:
        End of file. Exits the console.
        """
        return True

    def do_quit(self, line):
        """
        quit:
        Exits the console.
        """
        return True

    def emptyline(self):
        """If line is empty don't do anything (as opposed to execute previous
        command)."""
        pass

    def do_create(self, line):
        """
        create:

        Creates a new instance of BaseModel, saves it and prints the id.

        This method breaks a string of arguments down into smaller chunks,
        or strings. It will try to return the value of the named attribute.
        That will be stored, saved, and printed. If the named attribute
        doesn't exist, KeyError is raised and handled before "** class
        doesn't exist **" is printed to the screen.

        If the class name is missing, "** class name missing **" will be
        printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict[line]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, line):
        """
        show:

        Prints the string representation of an instance - class name and id

        This method splits the arguments into smaller strings before the
        arguments are used. If the length of the arguments is less than two,
        IndexError is raised, handled, and "** instance id missing **" will
        print to the screen since more than one argument is needed. However,
        if an appropriate amount of arguments is available, the result of
        class name and id will print to the screen. Otherwise, KeyError
        will be raised, handled and "** no instance found **" will be printed
        to the screen.

        If the class name is missing, "** class name missing **" will be
        printed to the screen. If the class name doesn't exist, "** class
        doesn't exist **" will be printed to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[obj_id])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        destroy:

        Deletes an instance based on the class name and id.

        This method requires two arguments, a class name and id. If the class
        name is missing, "** class name missing **" will be printed to the
        screen. If class name doesn't exist, "** class doesn't exist **"
        will be printed to the screen. If class name does exist, then the
        command will search for the id, or the second argument. If the id is
        missing, IndexError is raised and "** instance id missing **" will
        print to the screen. However, if found, the instance will be deleted.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """
        all:

        Prints all string representation of all instances based or not on
        the class name.

        This method will print out the string representation of the value
        of every instance of a class or not a class. If the class doesn't
        exist, "** class doesn't exist **" will print to the screen.
        """
        if len(line) == 0:
            print([str(v) for v in models.storage.all().values()])
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in models.storage.all().items()
                   if line in k])

    def do_update(self, line):
        """
        update:

        Updates an instance based on the class name and id by adding or
        updating attribute.

        This method can only update one attribute at a time. Attributes
        "created_at", "updated_at", and "id" should't be updated with this
        method.

        If the class name is missing, "** class name missing **" is printed
        to the screen. If the class name doesn't exist, print "** class
        doesn't exist **".

        If id is missing, "** instance id missing **" is printed to the screen.
        If the attribute name is missing, "** attribute name missing **"
        will be printed to the screen. If the value for the attribute name
        doesn't exist, "** value missing **" will print to screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    setattr(obj, attr, val)
                                except AttributeError:
                                    print("** cannot set val: {}".format(val) +
                                          " for attr: ({}) **".format(attr))
                                else:
                                    obj.save()
            else:
                print("** class doesn't exist **")

    def do_count(self, line):
        """
        Usage: count [<class>]

        Count the number of instances of `class` if provided, otherwise
        the total number of instances in memory.
        """
        if len(line) == 0:
            print(len([str(v) for v in models.storage.all().values()]))
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print(len([str(v) for k, v in models.storage.all().items()
                       if line in k]))

    def do_BaseModel(self, line):
        """Usage: BaseModel.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'BaseModel', args]))

    def do_User(self, line):
        """Usage: User.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'User', args]))

    def do_State(self, line):
        """Usage: State.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'State', args]))

    def do_City(self, line):
        """Usage: City.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'City', args]))

    def do_Amenity(self, line):
        """Usage: Amenity.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Amenity', args]))

    def do_Place(self, line):
        """Usage: Place.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Place', args]))

    def do_Review(self, line):
        """Usage: Review.<cmd>([args, ...])

        `cmd` can be any of:
            all, show, update, destroy, or create

        Arguments are the same and in the same order as for other
        commands.
        """
        cmd, args = parse(line)
        self.onecmd(' '.join([cmd, 'Review', args]))


def parse(line):
    """Parse method-like command.

    Args:
        line (str): method call with arguments (e.g. `.all(arg1, arg2)`
    """
    pattern = '\.([^.]+)\(|[\s,()]*([^(),]+)[\s,()]*'
    args = re.findall(pattern, line)
    cmd = args[0][0]
    try:
        args = args[1:]
    except IndexError:
        line = ''
    else:
        line = ' '.join(map(lambda x: x[1].strip('"'), args))
    return cmd, line


if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()
