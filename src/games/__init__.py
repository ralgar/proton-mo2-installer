'''
This module contains a list of maps of game app_ids to their classes.
'''

from games.skyrim_le import SkyrimLE
from games.skyrim_se import SkyrimSE

games = {
    72850: {
        "name": "Skyrim LE",
        "init": SkyrimLE()
    },
    489830: {
        "name": "Skyrim SE",
        "init": SkyrimSE()
    }
}
