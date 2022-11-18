'''
This module contains the TUI object and methods.
'''

import logging
import os

from pmf import games
from pmf import platforms


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
        game.install()
        print("\nSuccessfully installed MO2 in", game.mo2_dir, "!\n")


    def main(self):

        platform = self.select_platform()
        game = self.select_game(platform)
        task = self.select_task()

        if task == "Install":
            self.install_tools(game)
        elif task == "Uninstall":
            self.install_tools(game)
        elif task == "Upgrade":
            self.install_tools(game)


    def select_platform(self):
        '''
        Searches for Steam root candidates and, if there are more
        than one, asks the user to choose from them.
        '''

        self.init_screen()

        for i, val in enumerate(platforms.platforms):
            print(str(i+1) + ":", val)
        answer = int(input("\nChoose a platform: ")) - 1

        if answer == 0:
            return platforms.steam.Steam()
        if answer == 1:
            return platforms.steam.SteamFlatpak()

        raise Exception('Invalid platform choice.')


    def select_game(self, platform):
        '''
        Scans for games which are both supported and installed, and
        asks the user to choose from them.
        '''

        self.init_screen()

        steam_apps = platform.list_appids()

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
        return games.init(platform, appid)


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
