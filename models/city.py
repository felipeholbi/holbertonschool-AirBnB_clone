#!/usr/bin/python3
""" class City """


from City(BaseModel):
    """class City that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize city clas"""
        super().__init__(*args, **Kwargs)
