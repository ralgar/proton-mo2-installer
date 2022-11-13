#!/usr/bin/env python3

'''
Main module
'''

import os

import tui


def main():
    '''
    Main function.
    '''

    ui = tui.Tui()

    steam_root = ui.select_steam_root(os.getenv('HOME'))

    print(steam_root)


if __name__ == "__main__":
    main()
