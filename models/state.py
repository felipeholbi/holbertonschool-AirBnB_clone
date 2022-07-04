#!/usr/bin/python3
"""class state"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    ...
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)
