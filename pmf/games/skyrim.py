from os import path

from pmf import mod_tools, utils

class Skyrim:

    def __init__(self, db, platform):
        self.app_id          = 0
        self.executable      = ''
        self.name            = ''
        self.nexus_id        = ''
        self.protontricks    = []
        self.script_extender = ''
        self.db              = db
        self.platform        = platform

    @property
    def db_instance_id(self):
        return self.db.instance_id(self.platform.name)

    @property
    def game_dir(self):
        return path.join(self.library_root, 'common', self.subdirectory)

    @property
    def library_root(self):
        library_root, val = self.platform.read_game_info(self.app_id)
        return library_root

    @property
    def mo2_dir(self):
        return path.join(utils.get_data_dir(), self.nexus_id)

    @property
    def subdirectory(self):
        val, subdirectory = self.platform.read_game_info(self.app_id)
        return subdirectory

    def install(self):
        mod_tools.mo2.install(self, self.mo2_dir)
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
        archive = utils.download_file(self.script_extender)
        utils.extract_archive(self, self.game_dir, archive, 1)

    def install_workarounds(self):
        mod_tools.fnis.install(path.join(self.game_dir, 'Data'))

class SkyrimLE(Skyrim):

    def __init__(self, db, platform):

        super().__init__(db, platform)
        self.app_id          = 72850
        self.executable      = "SkyrimLauncher.exe"
        self.name            = "Skyrim Legendary Edition"
        self.nexus_id        = "skyrim"
        self.protontricks    = [ "d3dcompiler_43", "d3dx9" ]
        self.script_extender = 'https://skse.silverlock.org/beta/skse_1_07_03.7z'

class SkyrimSE(Skyrim):

    def __init__(self, db, platform):

        super().__init__(db, platform)
        self.app_id          = 489830
        self.executable      = "SkyrimSELauncher.exe"
        self.name            = "Skyrim Special Edition"
        self.nexus_id        = "skyrimspecialedition"
        self.protontricks    = [ "xaudio2_7=native" ]
        self.script_extender = 'https://skse.silverlock.org/beta/skse64_2_02_03.7z'
