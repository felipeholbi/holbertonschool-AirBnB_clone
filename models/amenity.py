#!/usr/bin/python3
"""class Amenity"""


class Amenity(BaseModel):
    """class Amenity that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity clas"""
        super().__init__(*args, **kwargs)
