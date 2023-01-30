import logging
import os
import vdf

from pmf import utils

class Steam:

    def __init__(self):
        self.name = 'Steam'
        self.root = self.find_root(os.getenv('HOME'))

    @property
    def compat_tools_path(self):
        return os.path.join(self.root, 'compatibilitytools.d')

    @property
    def global_config(self):
        return os.path.join(self.root, 'config', 'config.vdf')

    def find_root(self, path):
        '''
        Returns a list of all possible Steam root paths.
        '''

        name   = "config.vdf"
        ignore = os.path.join(path, '.var/app/com.valvesoftware.Steam')
        result = []

        for root, _, files in os.walk(path):
            if not root.startswith(ignore):
                if name in files:
                    result.append(os.path.dirname(root))

        if len(result) > 1:
            logging.critical('Found more than 1 Steam installation')
            raise Exception('Found more than 1 Steam installation')
        if len(result) < 1:
            logging.critical('Could not find a Steam installation')
            raise Exception('Could not find a Steam installation')

        return result[0]

    def install_compat_tool(self, db, game, url):
        if not os.path.isdir(self.compat_tools_path):
            os.mkdir(self.compat_tools_path)
        archive = utils.download_file(url)
        utils.extract_archive(db, game, self.compat_tools_path, archive)

    def list_appids(self):
        '''
        Lists all AppIDs installed for a given Steam instance.
        '''

        # Search for the root library VDF
        for library in '/steamapps', '/steam':
            if os.path.isfile(self.root + library + '/libraryfolders.vdf'):
                vdf_file = self.root + library + '/libraryfolders.vdf'
                break

        if not vdf_file:
            logging.critical('Could not find Steam root library')
            raise Exception('Could not find Steam root libary')

        # Build a list of AppIDs from all libraries
        apps = []
        with open(vdf_file, encoding='utf-8') as file:
            vdf_data = vdf.parse(file)
            for entry in vdf_data['libraryfolders']:
                if not entry == 'contentstatsid':
                    for app in vdf_data['libraryfolders'][entry]['apps']:
                        apps.append(int(app))

        if len(apps) < 1:
            logging.critical('Could not find a Steam installation')
            raise Exception('Could not find a Steam installation')

        return apps

    def read_game_info(self, appid):

        root_vdf_file = os.path.join(self.root, 'steamapps', 'libraryfolders.vdf')

        # Find the library_path for the given AppID
        with open(root_vdf_file, 'r', encoding='utf-8') as file:
            vdf_data = vdf.parse(file)
            for entry in vdf_data['libraryfolders']:
                if not entry == 'contentstatsid':
                    for app in vdf_data['libraryfolders'][entry]['apps']:
                        if appid == int(app):
                            library_root = vdf_data['libraryfolders'][entry]['path']
                            library_root = os.path.join(library_root, 'steamapps')

        # Find the subdirectory of the given AppID
        app_acf_file  = 'appmanifest_' + str(appid) + '.acf'
        app_acf_file  = os.path.join(library_root, app_acf_file)
        with open(app_acf_file, 'r', encoding='utf-8') as file:
            app_stat     = vdf.parse(file)['AppState']
            subdirectory = app_stat['installdir']

        return library_root, subdirectory

    def set_compat_tool(self, app_id, compat_tool):

        skel = {
            'name': compat_tool,
            'config': '',
            'priority': '250'
        }

        with open(self.global_config, 'r', encoding='UTF-8') as fp:
            data = vdf.parse(fp)

        steam = data['InstallConfigStore']['Software']['Valve']['Steam']
        if str(app_id) not in steam['CompatToolMapping']:
            steam[str(app_id)] = skel
            steam['CompatToolMapping'][str(app_id)] = skel
        else:
            steam['CompatToolMapping'][str(app_id)]['name'] = compat_tool

        data['InstallConfigStore']['Software']['Valve']['Steam'] = steam
        with open(self.global_config, 'w', encoding='UTF-8') as fp:
            fp.write(vdf.dumps(data, pretty=True))


class SteamFlatpak(Steam):

    def __init__(self):
        super().__init__()
        self.name = 'Steam Flatpak'
        root = os.path.join(os.getenv('HOME'), '.var/app/com.valvesoftware.Steam')
        self.root = self.find_root(root)
