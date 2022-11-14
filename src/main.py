#!/usr/bin/env python3

'''
Main module
'''

import logging

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

    tui = Tui()

    steam_root = tui.select_steam_root()
    game = tui.select_game(steam_root)
    task = tui.select_task()

    if task == "Install":
        tui.install_tools(game)
    elif task == "Uninstall":
        tui.install_tools(game)
    elif task == "Upgrade":
        tui.install_tools(game)


if __name__ == "__main__":
    main()
