#!/usr/bin/env python3

import logging
import sys

from tui import Tui

def main():
    '''
    Main function.
    '''

    logging.basicConfig(
        filename='setup.log',
        format='[%(levelname)s] %(asctime)s :: %(message)s',
        encoding='utf-8',
        level=logging.DEBUG
    )
    logging.info("===========================================================")

    try:
        assert 'linux' in sys.platform
    except AssertionError:
        print('This tool is designed to run on Linux only. Exiting.')

    tui = Tui()
    tui.main()

if __name__ == "__main__":
    main()
