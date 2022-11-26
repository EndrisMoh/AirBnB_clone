#!/usr/bin/python3
"""
Class for user's review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews made by users about a place"""
    place_id = ""
    user_id = ""
    text = ""
