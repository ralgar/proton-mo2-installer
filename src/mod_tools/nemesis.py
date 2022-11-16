from os import path, makedirs

def install(game_data_path):

    d = path.join(game_data_path, 'Nemesis_Engine')
    if not path.isdir(d):
        makedirs(d)
