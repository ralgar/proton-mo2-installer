#!/usr/bin/env python
'''
Changes a compatibility tool mapping in Steam's config.vdf.
'''

import getopt
import sys
import vdf


def main(argv):
    '''
    Main function. Parses args.
    '''

    arg_appid       = ""
    arg_config_file = ""
    arg_compat_tool = ""
    arg_list = False

    try:
        opts, args = getopt.getopt(
            argv[1:], "a:c:h:l:t:", ["appid", "config", "help", "list", "tool"])
        if len(opts) != 3:
            printHelp()
            return False
    except getopt.GetoptError:
        printHelp()
        return False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printHelp()
            return False
        if opt in ("-a", "--appid"):
            arg_appid = arg
        if opt in ("-c", "--config"):
            arg_config_file = arg
        if opt in ("-t", "--tool"):
            arg_compat_tool = arg

    if opt in ("-l", "--list"):
        arg_list = True

    remapCompatTool(arg_appid, arg_config_file, arg_compat_tool, arg_list)

    return True


def printHelp():
    '''
    Prints the help dialog
    '''

    print("\nSteam Compat Tool Remapper\n")
    print("Usage:\n    compat-tool-remap.py -a <appid> -c <config_file> -t <compat_tool>")
    print("    compat-tool-remap.py -a <appid> -c <config_file> -l current\n")


def remapCompatTool(appid, config_file, compat_tool, bool_list):
    '''
    Remaps compatibility tool for a given appid.
    '''

    # Open the VDF file for reading
    with open(config_file, 'r', encoding='UTF-8') as fp:
        data = vdf.parse(fp)

    if bool_list:
        print(data['InstallConfigStore']['Software']['Valve']['Steam']\
            ['CompatToolMapping'][appid]['name'])
        return

    # Replace compat tool mapping
    data['InstallConfigStore']['Software']['Valve']['Steam']\
        ['CompatToolMapping'][appid]['name'] = compat_tool

    # Write the modified VDF data to file
    with open(config_file, 'w', encoding='UTF-8') as fp:
        fp.write(vdf.dumps(data, pretty=True))


if not main(sys.argv):
    sys.exit(1)
