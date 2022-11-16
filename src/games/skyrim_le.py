'''
This module provides an object class for Skyrim LE.
'''

from os import path

import mod_tools
import utils

class SkyrimLE:

    def __init__(self, library_root, subdirectory):

        self.app_id       = 72850
        self.executable   = "SkyrimLauncher.exe"
        self.name         = "Skyrim LE"
        self.nexus_id     = "skyrim"
        self.protontricks = [ "d3dcompiler_43", "d3dx9" ]

        self.library_root = library_root
        self.subdirectory = subdirectory

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
    def game_dir(self):
        return path.join(self.library_root, 'common', self.subdirectory)

    @property
    def mo2_dir(self):
        paths = utils.get_paths()
        return path.join(paths[3], self.nexus_id)

    def apply_workarounds(self):
        mod_tools.fnis.install(path.join(self.game_dir, 'Data'))
        mod_tools.nemesis.install(path.join(self.game_dir, 'Data'))
