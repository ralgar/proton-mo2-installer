from pmf.games.skyrim import SkyrimLE, SkyrimSE

# Provides names for AppIDs in the UI
games = {
    72850: "Skyrim LE",
    489830: "Skyrim SE"
}

def init(platform, appid):

    if appid == 72850:
        game = SkyrimLE(platform)
    if appid == 489830:
        game = SkyrimSE(platform)

    return game
