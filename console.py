#!/usr/bin/python3
""" A program that contains the entry point of the command interpreter """

import cmd
import shlex
from models import *


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class"""

    prompt = "(hbnb) "
    storage.reload()

    cls_list = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State',
                'Review']

    cmnd_list = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """ Parses input command"""
        if '.' in arg and '(' in arg and ')' in arg:
            clas = arg.split('.')
            cmnd = clas[1].split('(')
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
        all_objects = storage.all()
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
        else:
            dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            my_model = dct[args]()
            print(my_model.id)
            my_model.save()            

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
            class name and id. Ex: $ show BaseModel 1234-1234-1234
        """

        if not arg:
            print("** class name missing **")
        return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instancs id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
        print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id\
            (save the change into the JSON file)\
            Usage: Example: $ destroy BaseModel 1234-1234-1234
        """

        if not arg:
            print("** class name missing **")
        return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
            return
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances based or \
            not on the class name. Ex: $ all BaseModel or $ all.
        """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            instances_list = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    instances_list += [value.__str__()]
            print(instances_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or \
            updating attribute (save the change into the JSON file) \
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". \
            Usage:update <class name> <id> <attribute name> "<attribute value>\
            Only one attribute can be updated at the time \
            You can assume the attribute name is valid (exists for this model)\
            The attribute value must be casted to the attribute type\
            Only “simple” arguments can be updated: string, integer and float.\
            You can assume nobody will try to update list of ids or datetime
        """

        if not arg:
            print("** class name missing **")
        return

        quote = ""
        for argv in arg.split(','):
            quote = quote + argv

        args = shlex.split(quote)

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            all_objects = storage.all()
            for key, objc in all_objects.items():
                obj_name = objc.__class__.__name__
                obj_id = objc.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ Ctrl + D command to exit the command interpreter """
        return True

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
                except:
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
