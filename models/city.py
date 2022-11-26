#!/usr/bin/python3

"""
Class defines city that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel
    Attributes:
        state_id (str): Public class attribute for city's state_id
        name (str): Public class attribute for city's name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for city class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
