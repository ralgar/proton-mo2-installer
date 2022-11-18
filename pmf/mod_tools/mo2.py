'''
This module provides functions for interacting with Mod Organizer 2.
'''

import logging
from os import path, makedirs, chmod
import shutil
import sys

import pmf
from pmf import utils


def install(game):
    '''
    Installs Mod Organizer 2.
    '''

    mo2_version = "2.4.4"

    url_base = "https://github.com/ModOrganizer2/modorganizer/releases/download/"
    url_file = "v" + mo2_version + "/Mod.Organizer-" + mo2_version + ".7z"
    full_url = url_base + url_file
    install_dir = path.join(game.data_dir, game.nexus_id)

    mo2_archive = utils.download_file(full_url)
    utils.extract_archive(game, install_dir, mo2_archive)

    install_nxm_handler(game)


def install_nxm_handler(game):
    '''
    Installs NXM handler functions, and scripts.
    '''

    source_dir = path.dirname(pmf.__file__)
    source_dir = path.join(source_dir, 'resources')

    source_desktop_file = path.join(source_dir, 'nxm-handler.desktop')
    dest_desktop_file   = path.join(game.data_home, 'applications')
    dest_desktop_file   = path.join(dest_desktop_file, 'nxm-handler.desktop')

    source_script_file = path.join(source_dir, 'nxm-broker.sh')
    dest_script_file   = path.join(utils.bin_dir(), 'nxm-broker.sh')

    # Ensure the applications (.desktop) directory exists
    if not path.isdir(path.dirname(dest_desktop_file)):
        makedirs(path.dirname(dest_desktop_file), 0o755)

    # Copy and track the files, set perms
    shutil.copyfile(source_desktop_file, dest_desktop_file)
    utils.track_file(game, dest_desktop_file)
    shutil.copyfile(source_script_file, dest_script_file)
    chmod(dest_script_file, 0o744)
    utils.track_file(game, dest_script_file)
