'''
This module provides an object class for Skyrim LE.
'''

from os import path

import utils

class SkyrimLE:

    def __init__(self):

        self.app_id       = 72850
        self.executable   = "SkyrimLauncher.exe"
        self.name         = "Skyrim LE"
        self.nexus_id     = "skyrim"
        self.protontricks = [ "d3dcompiler_43", "d3dx9" ]
        self.subdirectory = "Skyrim"

    def __str__(self):

        describe = {
            "app_id":       self.app_id,
            "executable":   self.executable,
            "name":         self.name,
            "nexus_id":     self.nexus_id,
            "protontricks": self.protontricks,
            "subdirectory": self.subdirectory,
        }

        return str(describe)

    @property
    def bin_dir(self):
        return utils.get_paths()[0]

    @property
    def cache_dir(self):
        return utils.get_paths()[1]

    @property
    def cache_home(self):
        return utils.get_paths()[2]

    @property
    def data_dir(self):
        return utils.get_paths()[3]

    @property
    def data_home(self):
        return utils.get_paths()[4]

    @property
    def mo2_dir(self):
        paths = utils.get_paths()
        return path.join(paths[3], self.nexus_id)
