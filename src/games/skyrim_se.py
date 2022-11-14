'''
This module provides an object for Skyrim SE.
'''

class SkyrimSE:

    def __init__(self):

        self.app_id = 489830
        self.name   = "Skyrim SE"


    def __str__(self):

        self_dict = {
            "app_id": self.app_id,
            "name": self.name
        }

        return str(self_dict)
