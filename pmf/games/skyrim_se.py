from os import mkdir, path

from pmf import mod_tools, utils

class SkyrimSE:

    def __init__(self, platform):

        self.app_id       = 489830
        self.executable   = "SkyrimSELauncher.exe"
        self.name         = "Skyrim SE"
        self.nexus_id     = "skyrimspecialedition"
        self.protontricks = [ "xaudio2_7=native" ]
        self.platform     = platform

    @property
    def data_dir(self):
        return utils.get_paths()[0]

    @property
    def data_home(self):
        return utils.get_paths()[1]

    @property
    def game_dir(self):
        return path.join(self.library_root, 'common', self.subdirectory)

    @property
    def library_root(self):
        library_root, val = self.platform.read_game_info(self.app_id)
        return library_root

    @property
    def mo2_dir(self):
        paths = utils.get_paths()
        return path.join(paths[0], self.nexus_id)

    @property
    def subdirectory(self):
        val, subdirectory = self.platform.read_game_info(self.app_id)
        return subdirectory

    def install(self):
        mod_tools.mo2.install(self)
        mod_tools.proton_shunt.install(self)
        self.install_script_extender()
        self.install_workarounds()
        self.install_custom_proton()

    def install_custom_proton(self):
        url = 'https://github.com/ralgar/proton-builds/releases/download'
        url = path.join(url, 'Proton-6.17-STL-1/Proton-6.17-STL-1.tar.gz')
        self.platform.install_compat_tool(self, url)
        self.platform.set_compat_tool(self.app_id, 'Proton-6.17-STL-1')

    def install_script_extender(self):
        url = 'https://github.com/ianpatt/skse64/releases/download'
        url = path.join(url, 'v2.2.3/skse64_2_02_03.7z')
        archive = utils.download_file(url)
        utils.extract_archive(self, self.game_dir, archive, 1)

    def install_workarounds(self):
        mod_tools.fnis.install(path.join(self.game_dir, 'Data'))
        mod_tools.nemesis.install(path.join(self.game_dir, 'Data'))
