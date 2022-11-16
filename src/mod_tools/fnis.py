from os import path, makedirs

def install(game_data_path):

    base = path.join(game_data_path, 'tools')
    dirs = [
        path.join(base, 'GenerateFNIS_for_Modders'),
        path.join(base, 'GenerateFNIS_for_Users')
    ]
    for d in dirs:
        if not path.isdir(d):
            makedirs(d)
