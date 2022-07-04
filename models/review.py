#!/usr/bin/python3
""" class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    ...
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize Review"""
        super().__inti__(*args, **kwargs)
