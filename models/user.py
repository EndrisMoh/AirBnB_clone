#!/usr/bin/python3
"""
User class creation that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
