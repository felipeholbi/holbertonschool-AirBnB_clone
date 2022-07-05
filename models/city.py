#!/usr/bin/python3
""" class City """
from models.base_model import BaseModel

class City(BaseModel):
    """
    ...
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize city"""
        super().__init__(*args, **Kwargs)
