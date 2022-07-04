#!/usr/bin/python3
"""class Amenity"""


class Amenity(BaseModel):
    """
    ...
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
