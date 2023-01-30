'''
This module provides functions for interacting with Mod Organizer 2.
'''

from os import path, makedirs, chmod
import shutil

import pmf
from pmf import utils


def install(db, game, install_path):

    mo2_version = "2.4.4"

    url_base = "https://github.com/ModOrganizer2/modorganizer/releases/download/"
    url_file = "v" + mo2_version + "/Mod.Organizer-" + mo2_version + ".7z"
    full_url = url_base + url_file

    mo2_archive = utils.download_file(full_url)
    utils.extract_archive(db, game, install_path, mo2_archive)

    install_nxm_handler(db, game, path.dirname(install_path))


def install_nxm_handler(db, game, data_dir):
    '''
    Installs NXM handler functions, and scripts.
    '''

    source_dir = path.dirname(pmf.__file__)
    source_dir = path.join(source_dir, 'resources')

    source_desktop_file = path.join(source_dir, 'nxm-handler.desktop')
    dest_desktop_file   = path.join(path.dirname(data_dir), 'applications')
    dest_desktop_file   = path.join(dest_desktop_file, 'nxm-handler.desktop')

    source_script_file = path.join(source_dir, 'nxm-broker.sh')
    dest_script_file   = path.join(utils.get_bin_dir(), 'nxm-broker.sh')

    # Ensure the applications (.desktop) directory exists
    if not path.isdir(path.dirname(dest_desktop_file)):
        makedirs(path.dirname(dest_desktop_file), 0o755)

    # Copy and track the files, set perms
    shutil.copyfile(source_desktop_file, dest_desktop_file)
    db.track_file(db.instance_id(game.platform.name), dest_desktop_file)
    shutil.copyfile(source_script_file, dest_script_file)
    chmod(dest_script_file, 0o744)
    db.track_file(db.instance_id(game.platform.name), dest_script_file)
