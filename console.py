#!/usr/bin/python3
""" A program that contains the entry point of the command interpreter """

import cmd
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """ Command interpreter class"""

    prompt = "(hbnb) "

    classes_list = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']

    commands_list = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """ Parses input command"""
        if '.' in arg and '(' in arg and ')' in arg:
            clas = arg.split('.'
            cmnd = clas[1].split('(')
            args = cmnd[1].split(')')
                if clas[0] in HBNBCommand.classes_list and cmnd[0] in commamds_list:
                    arg  = cmnd[0] + ' ' + clas[0] + ' ' + args[0]
        return arg

    def help_help(self):
        """ Prints the help command description"""
        print("Provides the description of a given command")    

    def empltyline(self):
        """ Does nothing when there is empty line + Enter key """
        pass

    def do_count(self, class_name)
        """ Counts the number of instances in a class"""
        count = 0
        all_objects = storage.all()
        for key, value in all_objects.items():
            clss = key.split('.')
            if clss[0] == class_name:
                count = count + 1
        print(count)

    def do_create(self, type_model):
        """ Creates a new instance of a BaseModel parent class, saves it (to the JSON file) and prints the id.
            Ex: $ create BaseModel """

		if not type_model:
			print("** class name missing **")
		elif type_model not in HBNBCommand.classes_list:
			print("** class doesn't exist **")
		else:
			dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'City': City, 'Amenity': Amenity, 'State': State, 'Review': Review}
			my_model = dct[type_model]() 
			print(my_model.id)
			my_model.save()

	def do_show(self, arg):
		""" Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234 """
	
		if not arg:
			print("** class name missing **")
		return

		args = arg.split(' ')
	
		if args[0] not in HBNBCommand.classes_list
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instancs id missing **")
		else:
			all_objects = storage.all()
			for key, value in all_objects.items():
			obj_name = value.__class__.__name__
			obj_id = value.id
			if obj_name == args[0] and obj_id == args[1].strip('"'):
				print(value)
			return
		print("** no instance found **")

	def do_destroy(self, arg):
		""" Deletes an instance based on the class name and id (save the change into the JSON file) Ex: $ destroy BaseModel 1234-1234-1234 """
	
		if not arg:
			print("** class name missing **")
		return 

		args = arg.split(' ')

		if args[0] not in HBNBCommand.classes_list:
			print("** class doesn't exist **")
		elif:
			all_objects = storage.all()
			for key, value in all_objects.items():
			obj_name = value.__class__.__name__
			obj_id = value.id
				if obj_name == args[0] and obj_id == args[1].strip('"'):
					del value
					del storage._FileStorage__objects[key]
					storage.save()
				return
			print("** no instance found **")

	def do_all(self, arg):
		""" Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all. """

		if not arg:
			print("** class name missing **")
			return

		args = arg.split(' ')

		if args[0] not in HBNBCommand.classes_list:
			print("** class doesn't exist **")
		else:
			all_objects = storage.all()
			instances_list = []
			for key, value in all_objects.items():
				obj_name = value.__class__.__name__
				if obj_name == args[0]:
					instances_list += [value.__str__()]
			print(instances_list)

	def do_update(self, arg):
		""" Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com". Usage: update <class name> <id> <attribute name> "<attribute value> Only one attribute can be updated at the time You can assume the attribute name is valid (exists for this model) The attribute value must be casted to the attribute type  Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime """

		if not arg:
			print("** class name missing **")
			return

		quote = ""
		for argv in arg.split(','):
			quote = quote + argv

		args = shlex.split(quote)

		if args[0] not in HBNBCommand.classes_list:
			print("** class doesn't exist **")
		elif len(args) == 1:
			print("** instance id missing **")
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
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
