'''
This module contains utility functions.
'''

import logging
import os
import sys

import libarchive
import requests


def download_file(dest_dir, url):
    '''
    Downloads a file from the provided URL to the dest_dir, if it's not
    already present. Creates the destination path if needed.
    '''

    filename  = url.split('/')[-1]
    full_path = dest_dir + '/' + filename

    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir, 0o755)

    if not os.path.isfile(full_path):
        data = requests.get(url, stream=True, timeout=15)
        with open(full_path, 'wb') as file:
            for chunk in data.iter_content(chunk_size=4096):
                file.write(chunk)
        logging.info("Finished downloading file: %s", filename)
    else:
        logging.info("File already present: %s", filename)

    return full_path


def extract_archive(game, dest, archive, strip_leading=0):
    '''
    Extracts an archive to a destination directory. Optionally strips
    (int) leading directories, for archives with a nested structure.
    '''

    # Ensure dest exists
    if not os.path.isdir(dest):
        os.makedirs(dest, 0o755)
    track_file(game, dest)

    with libarchive.file_reader(archive) as a:
        cwd = os.getcwd()
        os.chdir(dest)
        for entry in a:

            # Strip i leading directories, and skip empty indexes
            skip = False
            for i in range(strip_leading):
                entry.pathname = "/".join(entry.pathname.split('/')[1:])
                if len(entry.pathname) == 0:
                    skip = True
            if skip is True:
                continue

            libarchive.extract.extract_entries([entry])
            track_file(game, os.path.join(dest, entry.pathname))

        os.chdir(cwd)

def bin_dir():

    bin_dir = os.path.join(os.getenv('HOME'), '.local/bin')
    if bin_dir not in os.getenv('PATH'):
        logging.critical('Could not find %s in PATH.', bin_dir)
        sys.exit(1)

    return bin_dir

def get_paths():
    '''
    Discovers local paths (XDG Dirs, user PATH, etc.)
    '''

    if os.getenv('XDG_CACHE_HOME'):
        cache_home = os.getenv('XDG_CACHE_HOME')
    else:
        cache_home = os.path.join(os.getenv('HOME'), '.cache')
    cache_dir = os.path.join(cache_home, "proton-mo2-installer")

    if os.getenv('XDG_DATA_HOME'):
        data_home = os.getenv('XDG_DATA_HOME')
    else:
        data_home = os.path.join(os.getenv('HOME'), '.local/share')
    data_dir = os.path.join(data_home, "proton-mo2-installer")

    return [ cache_home, cache_dir, data_dir, data_home ]


def track_file(game, file):
    '''
    Adds a file/dir to the database list, ignoring duplicate entries.
    '''

    database = os.path.join(game.mo2_dir, "tracked.db")

    unique = True
    with open(database, 'a+', encoding='UTF-8') as fp:
        fp.seek(0)
        for line in fp.readlines():
            if line.strip() == file:
                unique = False

        if unique is True:
            fp.seek(0, 2)
            fp.write(file + '\n')
