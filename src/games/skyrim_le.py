'''
This module provides an object for Skyrim LE.
'''

class SkyrimLE:

    def __init__(self):

        self.app_id = 72850
        self.name   = "Skyrim LE"


    def __str__(self):

        self_dict = {
            "app_id": self.app_id,
            "name": self.name
        }

        return str(self_dict)
