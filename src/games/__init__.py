'''
This module contains a list of maps of game app_ids to their classes.
'''

from games.skyrim_le import SkyrimLE
from games.skyrim_se import SkyrimSE

games = {
    72850: "Skyrim LE",
    489830: "Skyrim SE"
}

def init(steam_root, appid, library_root, subdirectory):

    if appid == 72850:
        game = SkyrimLE(steam_root, library_root, subdirectory)
    if appid == 489830:
        game = SkyrimSE(steam_root, library_root, subdirectory)

    return game
