'''
This module contains utility functions.
'''

import logging
import os
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
        print(":: Downloading file:", filename, '...')
        data = requests.get(url, stream=True, timeout=15)
        with open(full_path, 'wb') as file:
            for chunk in data.iter_content(chunk_size=4096):
                file.write(chunk)
        logging.info("Finished downloading file: %s", filename)
    else:
        logging.info("File already present: %s", filename)

    return full_path


def extract_archive(dest_dir, archive, strip_leading=0):
    '''
    Extracts an archive.
    '''

    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir, 0o755)

    command = "bsdtar -C " + dest_dir
    command = command + " --strip-components " + str(strip_leading)
    command = command + " -xvf " + archive

    os.system(command)
