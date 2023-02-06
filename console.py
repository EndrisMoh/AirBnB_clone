#!/usr/bin/python3
""" A program that contains the entry point of the command interpreter """


import cmd
<<<<<<< HEAD
import shlex
import models
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
=======
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
>>>>>>> aa5b201271d827d4bb071ebc69921fbb7820e01c


class HBNBCommand(cmd.Cmd):
    """ HBNH command interpreter console """
    prompt = '(hbnb) '

<<<<<<< HEAD
    prompt = "(hbnb) "
    #storage.reload()
=======
    def do_EOF(self, arg):
        """Exits console"""
        return True
>>>>>>> aa5b201271d827d4bb071ebc69921fbb7820e01c

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

<<<<<<< HEAD
    def precmd(self, arg):
        """ Parses input command"""
        if '.' in arg and '(' in arg and ')' in arg:
            clas = arg.split('.')
            cmnd_list = clas[1].split('(')
            args = cmnd[1].split(')')
            if clas[0] in HBNBCommand.cls_list and cmnd[0] in cmnd_list:
                arg = cmnd[0] + ' ' + clas[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints the help command description"""
        print("Provides the description of a given command")

    def empltyline(self):
        """ Does nothing when there is empty line + Enter key """
        pass

    def do_count(self, class_name):
        """ Counts the number of instances in a class"""
        count = 0
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            clss = key.split('.')
            if clss[0] == class_name:
                count = count + 1
        print(count)

    def do_create(self, args):
        """ Creates a new instance of a BaseModel parent class,\
            saves it (to the JSON file) and prints the id.\
            Ex: $ create BaseModel
        """
        
        if not args:
            print("** class name missing **")       
        elif args not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
=======
    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except TypeError:
                        try:
                            value = float(value)
                        except TypeError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
>>>>>>> aa5b201271d827d4bb071ebc69921fbb7820e01c
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
<<<<<<< HEAD
            all_objs = models.storage.all()
            instances_list = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    instances_list += [value.__str__()]
            print(instances_list)
=======
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")
>>>>>>> aa5b201271d827d4bb071ebc69921fbb7820e01c

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except TypeError:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except TypeError:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_User(self, args):
        """Usages: User.action() to the user """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages: BaseModel.action() to the class BaseModel """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages: State.action() to the class State """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages: City.action() to the class City  """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages: Amenity.action() to the class Amenity """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages: Place.action() to the class Place """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages: Review.action() to the class Review """
        self.class_exec('Review', args)

    def class_exec(self, cls_name, args):
        """Wrapper function for <class name>.action()"""
        if args[:6] == '.all()':
            self.do_all(cls_name)
        elif args[:6] == '.show(':
            self.do_show(cls_name + ' ' + args[7:-2])
        elif args[:8] == ".count()":
            all_objs = {k: v for (k, v) in storage.all().items()
                        if isinstance(v, eval(cls_name))}
            print(len(all_objs))
        elif args[:9] == '.destroy(':
            self.do_destroy(cls_name + ' ' + args[10:-2])
        elif args[:8] == '.update(':
            if '{' in args and '}' in args:
                new_arg = args[8:-1].split('{')
                new_arg[1] = '{' + new_arg[1]
            else:
                new_arg = args[8:-1].split(',')
            if len(new_arg) == 3:
                new_arg = " ".join(new_arg)
                new_arg = new_arg.replace("\"", "")
                new_arg = new_arg.replace("  ", " ")
                self.do_update(cls_name + ' ' + new_arg)
            elif len(new_arg) == 2:
                try:
                    dict = eval(new_arg[1])
                except TypeError:
                    return
                for j in dict.keys():
                    self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' ' +
                                   str(j) + ' ' + str(dict[j]))
            else:
                return
        else:
            print("Not a valid command")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
