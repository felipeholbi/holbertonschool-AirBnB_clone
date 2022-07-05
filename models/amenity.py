#!/usr/bin/python3
"""class Amenity"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    ...
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
