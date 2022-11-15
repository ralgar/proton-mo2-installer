'''
This module provides an object class for Skyrim LE.
'''

from os import getenv, path

class SkyrimLE:

    def __init__(self):

        self.app_id       = 72850
        self.executable   = "SkyrimLauncher.exe"
        self.name         = "Skyrim LE"
        self.nexus_id     = "skyrim"
        self.protontricks = [ "d3dcompiler_43", "d3dx9" ]
        self.subdirectory = "Skyrim"

        if getenv('XDG_CACHE_HOME'):
            self.cache_home = getenv('XDG_CACHE_HOME')
        else:
            self.cache_home = path.join(getenv('HOME'), '.cache')
        self.cache_dir = path.join(self.cache_home, "proton-mo2-installer")

        if getenv('XDG_DATA_HOME'):
            self.data_home = getenv('XDG_DATA_HOME')
        else:
            self.data_home = path.join(getenv('HOME'), '.local/share')
        self.data_dir = path.join(self.data_home, "proton-mo2-installer")

        self.mo2_dir = path.join(self.data_dir, self.nexus_id)

        if path.join(getenv('HOME'), '.local/bin') in getenv('PATH'):
            self.bin_dir = path.join(getenv('HOME'), '.local/bin')


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
