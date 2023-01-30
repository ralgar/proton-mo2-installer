import logging
import sys

from pmf.gui import windows

def main():
    '''
    Main function.
    '''

    logging.basicConfig(
        filename='setup.log',
        format='[%(levelname)s] %(asctime)s :: %(message)s',
        encoding='utf-8',
        level=logging.DEBUG
    )
    logging.info("===========================================================")

    try:
        assert 'linux' in sys.platform
    except AssertionError:
        print('This tool is designed to run on Linux only. Exiting.')

    window = windows.MainWindow()
    window.mainloop()

if __name__ == "__main__":
    main()
