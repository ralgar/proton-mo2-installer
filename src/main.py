#!/usr/bin/env python3

'''
Main module
'''


from tui import Tui


def main():
    '''
    Main function.
    '''

    tui = Tui()

    steam_root = tui.select_steam_root()
    game = tui.select_game(steam_root)

    print(game)


if __name__ == "__main__":
    main()
