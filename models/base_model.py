#!/usr/bin/python3
"""
Parent class that will inherit to chilr classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Defines all common class attributes and methods
    """
    def __init__(self, *args, **kwargs)
	""" Initializes all attributes of the Base class
	"""
	if not kwargs:
	    self.id = str(uuid.uuid4)
