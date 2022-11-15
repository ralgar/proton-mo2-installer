'''
This module provides an object class for Skyrim SE.
'''

from os import getenv, path

class SkyrimSE:

    def __init__(self):

        self.app_id       = 489830
        self.executable    = "SkyrimSELauncher.exe"
        self.name         = "Skyrim SE"
        self.nexus_id     = "skyrimspecialedition"
        self.protontricks = [ "xaudio2_7=native" ]
        self.subdirectory = "Skyrim Special Edition"

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
