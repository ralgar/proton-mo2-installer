import logging
import os
import vdf

class SteamFlatpak:

    def __init__(self):
        self.name = 'Steam'
        root = os.path.join(os.getenv('HOME'), '.var/app/com.valvesoftware.Steam')
        self.root = self.find_root(root)

    def find_root(self, path):
        '''
        Returns a list of all possible Steam root paths.
        '''

        name   = "config.vdf"
        result = []

        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.dirname(root))

        if len(result) > 1:
            logging.critical('Found more than 1 Steam installation')
            raise Exception('Found more than 1 Steam installation')
        if len(result) < 1:
            logging.critical('Could not find a Steam installation')
            raise Exception('Could not find a Steam installation')

        return result[0]

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
