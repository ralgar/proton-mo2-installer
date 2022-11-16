'''
This module contains the TUI object and methods.
'''

import logging
import os

import mo2
import steam
import games


class Tui:
    '''
    Terminal User Interface (TUI) object.
    '''

    def __init__(self):

        self.init_screen()


    def init_screen(self):
        '''
        Clears and (re)initializes the screen.
        '''

        os.system('clear')
        print("\n\033[1;4mWelcome to Proton MO2 Installer v2!\033[0m\n\n")


    def install_tools(self, game):
        '''
        Installs the modding tools, and provides TUI updates on the process.
        '''

        self.init_screen()
        print("Installing...\n")

        mo2.install(game)

        if callable(getattr(game, 'apply_workarounds', None)):
            game.apply_workarounds()

        print("\nSuccessfully installed MO2 in", game.mo2_dir, "!\n")


    def select_steam_root(self):
        '''
        Searches for Steam root candidates and, if there are more
        than one, asks the user to choose from them.
        '''

        self.init_screen()

        candidates = steam.find_root(os.getenv('HOME'))
        if len(candidates) == 1:
            answer = 0
        elif len(candidates) > 1:
            for i, val in enumerate(candidates):
                print(str(i+1) + ":", val[:-18])
            answer = int(input("\nChoose a Steam installation: ")) - 1
        else:
            return False

        steam_root = candidates[answer][:-18]

        return steam_root


    def select_game(self, steam_root):
        '''
        Scans for games which are both supported and installed, and
        asks the user to choose from them.
        '''

        self.init_screen()

        steam_apps = steam.list_appids(steam_root)

        # Make a list of supported AppIDs
        supported_apps = []
        for app in games.games:
            supported_apps.append(app)

        # Build a list of matching AppIDs
        matches = []
        for supported_app in supported_apps:
            for steam_app in steam_apps:
                if supported_app == steam_app:
                    matches.append(supported_app)

        # Have user select their chosen game
        for pos, match in enumerate(matches):
            print(str(pos+1) + ":", games.games[match])
        answer = int(input("\nChoose a game: ")) - 1
        appid = matches[answer-1]

        # Return an instantiated game object
        library_root, subdirectory = steam.read_game_info(appid, steam_root)
        return games.init(appid, library_root, subdirectory)


    def select_task(self):
        '''
        Prompts the user to select between Install, Uninstall, and
        Upgrade. Returns the name of the chosen task as a string.
        '''

        self.init_screen()

        tasks = [
            "Install",
            "Uninstall",
            "Upgrade"
        ]

        for pos, task in enumerate(tasks):
            print(str(pos+1) + ":", task)
        answer = int(input("\nChoose a task: ")) - 1

        return tasks[answer]
