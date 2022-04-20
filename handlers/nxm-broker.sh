#!/usr/bin/env bash
#
# nxm-broker.sh - Launcher script for the Mod Organizer 2 NXM Handler.
#
# This script is called by a MIME type handler, and simply launches
#   the NXM handler inside the prefix of a running MO2 instance.
# If MO2 isn't running, then we start it and pass the download as a launch argument.
#
# Copyright: (c) 2022, Ryan Algar (https://github.com/ralgar/proton-mo2-installer)
#
# GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


# Creates various GUI dialog boxes
_dialog() {

	local type
	local msg

    case $1 in
        error)
            type=error
            case $2 in
                invalid_url)
                    msg="\nAn invalid URL was provided. Aborting download."
                    ;;
                no_url)
                    msg="\nA URL was not provided. Cannot start download."
                    ;;
                missing_mo2)
                    msg="\nCannot find Mod Organizer 2 instance for game.\n\n$nexus_game_id"
                    ;;
                *)
                    return 1 ;;
            esac
            ;;
        *)
            return 1 ;;
    esac

    zenity \
        --title="NXM Handler" \
        --$type --icon-name "dialog-$type" \
        --no-wrap --ellipsize \
        --text "$msg"
}


# Check if an MO2 instance exists for Nexus Game ID
_get_mo2_instance_status() {

	if [ -d "$instance_dir" ]; then
		game_appid=$(cat "$instance_dir/appid.txt")
	else
        _dialog error missing_mo2
		return 1
	fi
}


# Main function
_main() {

	local game_appid
	local nxm_url="$1"
	local data_dir="${XDG_DATA_HOME:-$HOME/.local/share}"

	# Check and parse the NXM URL
	_parse_url "$nxm_url" || return 1

	# Make sure an MO2 instance exists for the game
	_get_mo2_instance_status || return 1

	# Start the download, and MO2 if necessary
	_start_download || return 1
}


# Checks and parses an NXM URL
_parse_url() {

	if [[ -z $* ]]; then
		echo "ERROR: Please specify an NXM URL to download."
        _dialog error no_url
		return 1
	elif [[ $# -gt 1 ]] ; then
		echo "ERROR: Too many arguments were passed."
        _dialog error invalid_url
		return 1
	elif [[ ! $nxm_url =~ nxm:// ]] ; then
		echo "ERROR: The NXM URL is malformed or otherwise invalid."
        _dialog error invalid_url
		return 1
	fi

	nexus_game_id=${nxm_url#nxm://}
	nexus_game_id=${nexus_game_id%%/*}

	instance_dir="$data_dir/proton-mo2-installer/modorganizer2/${nexus_game_id:?}"
}


_start_download() {

	# If MO2 is running, then pass the URL to it, else start MO2
	if pgrep -f "ModOrganizer.exe" ; then
		printf "INFO: Sending download to running Mod Organizer 2 instance.\n"
		if ! WINEESYNC=1 WINEFSYNC=1 protontricks-launch \
				--appid "$game_appid" "$instance_dir/nxmhandler.exe" "$nxm_url"
		then
			return 1
		fi
	else
		printf "INFO: MO2 is not running. launching it now.\n"
		if ! steam -applaunch "$game_appid" "$nxm_url" ; then
			return 1
		fi
	fi
}


if _main "$@" ; then
	exit 0
else
	exit 1
fi
