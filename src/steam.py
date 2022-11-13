'''
This module is responsible for interacting with Steam on Linux.
'''

import os

def find_root(path):
    '''
    Detects all possible Steam root paths. (Regular, and Flatpak)
    '''

    name = "config.vdf"
    result = []

    for root, dirs, files in os.walk(os.getenv('HOME')):
        if name in files:
            result.append(os.path.join(root, name))

    return result
