from os import chmod, path
from shutil import copy, move

from pmf import utils

def install(db, game):
    '''
    Installs Proton Shunt.
    '''

    version = "1.1.0"

    url_base = "https://github.com/ralgar/proton-shunt/releases/download/v" + version
    url_exec_file  = 'proton-shunt-v' + version + '.exe'
    url_conf_file  = 'proton-shunt.cfg'
    game_conf_file = path.join(game.game_dir, url_conf_file)
    game_exec_file = path.join(game.game_dir, game.executable)

    exec_file = utils.download_file(path.join(url_base, url_exec_file))
    conf_file = utils.download_file(path.join(url_base, url_conf_file))
    db.track_file(db.instance_id(game.platform.name), conf_file)

    if not path.isfile(game_conf_file):
        copy(conf_file, game_conf_file)

    if not path.isfile(game_exec_file + '.bak'):
        move(game_exec_file, game_exec_file + '.bak')
    copy(exec_file, game_exec_file)
    chmod(game_exec_file, 0o755)
    db.track_file(db.instance_id(game.platform.name), game_exec_file)
