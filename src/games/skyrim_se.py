'''
This module provides an object class for Skyrim SE.
'''

from os import path

import mod_tools
import utils

class SkyrimSE:

    def __init__(self, library_root, subdirectory):

        self.app_id       = 489830
        self.executable   = "SkyrimSELauncher.exe"
        self.name         = "Skyrim SE"
        self.nexus_id     = "skyrimspecialedition"
        self.protontricks = [ "xaudio2_7=native" ]

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

    def install(self):
        mod_tools.mo2.install(self)
        mod_tools.proton_shunt.install(self)
        self.install_script_extender()
        self.install_workarounds()

    def install_script_extender(self):
        url = 'https://github.com/ianpatt/skse64/releases/download'
        url = path.join(url, 'v2.2.3/skse64_2_02_03.7z')
        archive = utils.download_file(self.cache_dir, url)
        utils.extract_archive(self, self.game_dir, archive, 1)

    def install_workarounds(self):
        mod_tools.fnis.install(path.join(self.game_dir, 'Data'))
        mod_tools.nemesis.install(path.join(self.game_dir, 'Data'))
