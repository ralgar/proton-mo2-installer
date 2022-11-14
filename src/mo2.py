'''
This module provides functions for interacting with Mod Organizer 2.
'''

from os import path

import utils


def install(cache_dir, data_dir, game):
    '''
    Installs Mod Organizer 2.
    '''

    mo2_version = "2.4.4"

    url_base = "https://github.com/ModOrganizer2/modorganizer/releases/download/"
    url_file = "v" + mo2_version + "/Mod.Organizer-" + mo2_version + ".7z"
    full_url = url_base + url_file
    install_dir = path.join(data_dir, game.nexus_id)

    mo2_archive = utils.download_file(cache_dir, full_url)
    utils.extract_archive(install_dir, mo2_archive)

    print("\nSuccessfully installed MO2 in", install_dir, "!\n")
