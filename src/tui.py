'''
This module contains the TUI object and methods.
'''

import os

import steam


class Tui:
    '''
    TUI object.
    '''

    def __init__(self):

        print("\n\033[1;4mWelcome to Proton MO2 Installer v2!\033[0m\n")


    def select_steam_root(self, search_path):
        '''
        Searches for Steam root candidates and, if there are more
        than one, asks the user to choose from them.
        '''

        candidates = steam.find_root(os.getenv('HOME'))
        if len(candidates) == 1:
            answer = 0
        elif len(candidates) > 1:
            for i, val in enumerate(candidates):
                print(str(i+1) + ":", val[:-18])
            answer = int(input("\nChoose a Steam installation: ")) - 1
        else:
            return False

        return candidates[answer][:-18]


    def placeholder(self):

        return
