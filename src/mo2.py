'''
This module provides functions for interacting with Mod Organizer 2.
'''

import utils


def install(cache_dir, data_dir):
    '''
    Installs Mod Organizer 2.
    '''

    mo2_version = "2.4.4"

    url_base = "https://github.com/ModOrganizer2/modorganizer/releases/download/"
    url_file = "v" + mo2_version + "/Mod.Organizer-" + mo2_version + ".7z"
    full_url = url_base + url_file

    utils.download_file(cache_dir, full_url)
    print("\nSuccessfully installed MO2 in", data_dir, "!\n")
