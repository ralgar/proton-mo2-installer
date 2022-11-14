'''
This module is responsible for interacting with Steam on Linux.
'''

import logging
import os
import vdf


def find_game(appid):
    '''
    Finds the path to a game using its AppID.
    '''

    return appid


def find_root(path):
    '''
    Returns a list of all possible Steam root paths.
    '''

    name = "config.vdf"
    result = []

    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))

    return result


def list_appids(steam_root):
    '''
    Lists all AppIDs installed for a given Steam instance.
    '''

    # Search for the root library VDF
    for library in '/steamapps', '/steam':
        if os.path.isfile(steam_root + library + '/libraryfolders.vdf'):
            vdf_file = steam_root + library + '/libraryfolders.vdf'
            break

    # No Steam root found
    if not vdf_file:
        logging.critical('Could not find Steam root')
        return False

    # Read dict of libraries, and build a list of their AppIDs
    apps = []
    with open(vdf_file, encoding='utf-8') as file:
        vdf_data = vdf.parse(file)
        for entry in vdf_data['libraryfolders']:
            if not entry == 'contentstatsid':
                for app in vdf_data['libraryfolders'][entry]['apps']:
                    apps.append(int(app))

    return apps
