# Proton MO2 Installer
[![Latest Tag](https://img.shields.io/github/v/tag/ralgar/proton-mo2-installer?style=for-the-badge&logo=semver&logoColor=white)](https://github.com/ralgar/proton-mo2-installer/tags)
[![Software License](https://img.shields.io/github/license/ralgar/proton-mo2-installer?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Stars](https://img.shields.io/github/stars/ralgar/proton-mo2-installer?style=for-the-badge&logo=github&logoColor=white&color=gold)](https://github.com/ralgar/proton-mo2-installer)


## Overview
This project intends to make modding Bethesda games on Linux a reality for more users. It provides a set of scripts, which automatically configure a fully functional modding experience.

**Note:** The only tested game at this time is Skyrim SE. I don't own the other games on PC.

### Features
- [x] Simple, GUI-driven installer.
- [x] Installs Mod Organizer 2
- [x] Installs LOOT
- [x] Installs Script Extender
- [x] Launching the game from Steam now launches Mod Organizer 2 instead
- [x] NXM links from your browser can be sent to Mod Organizer 2
- [x] DynDoLOD, FNIS, Nemesis, BodySlide, Outfit Studio, and other tools all work as expected
- [ ] Steam Deck support (unsure, as I don't own one)
- [ ] Flatpak Steam support (experimental)


## Getting Started

### Prerequisites
You may need to manually install the following dependencies:
- bsdtar
- protontricks

These dependencies should be available out-of-the-box on most systems:
- curl
- xdg-utils
- zenity

### Installation
Installation is simple:
1. Install your chosen game through Steam.
2. Launch the game once to initialize the Proton prefix.
3. Grab the latest stable release of the installer [here](https://github.com/ralgar/proton-mo2-installer/releases), or simply `git clone` the repo.
4. Run `setup`, and follow the prompts until finished.
5. Launch the game. It will now launch MO2 instead.

**Note:** Installing the Windows packages can take a long time in some cases. There is no fix for this, just be patient.


### Configuring Mod Organizer 2
**On the first run of MO2:**
- You should create a *Portable* instance.
- MO2 will figure out the necessary paths automatically.
- Don't forget to connect your Nexus account.
- You will be asked whether MO2 should handle NXM links, you should choose *Yes*.

**Executable Paths:**
- To regain access to the game's launcher, edit the executable path in MO2 by simply appending `.bak` to the filename.
- To add LOOT as an executable, the path is `Z:\home\my_user\.local\share\proton-mo2-installer\tools\loot\LOOT.exe`.

**Installing Additional Modding Tools:**
1. Install the tool as a mod, using MO2.
2. Under the `Data` tab, find the executable, right click it, and choose `Add as Executable`.


## Supported Games

The following is a small overview of the current state of each supported game:<br>
Note: Much of this data is carried over from [modorganizer2-linux-installer](https://github.com/rockerbacon/modorganizer2-linux-installer)

| GAME                   | GAMEPLAY        | SCRIPT EXTENDER           | ENB           |
| :--------------------- | :-------------- | :------------------------ | :------------ |
| Fallout 3              | not tested      | not tested                | not tested    |
| Fallout 4              | working         | [some plugins might not work](https://github.com/rockerbacon/modorganizer2-linux-installer/issues/32) | ENB v0.393 or older, disabling "EnablePostPassShader" might be necessary |
| Fallout New Vegas      | fullscreen only | working                   | working       |
| Morrowind              | not tested      | not tested                | not tested    |
| Oblivion               | working         | [some plugins might require manual setup](https://github.com/rockerbacon/modorganizer2-linux-installer/issues/63#issuecomment-643690247)                 | not tested    |
| Skyrim                 | working         | working                   | working       |
| Skyrim Special Edition | working         | working                   | working       |

For known bugs and workarounds, please refer to the [issues page](https://github.com/ralgar/proton-mo2-installer/issues?q=is:issue+is:open+label:bug+)

Please help to keep this table up to date by [opening issues](https://github.com/ralgar/proton-mo2-installer/issues/new/choose) with any problems you encounter.


## Updating the tools

Updating the tools probably isn't necessary at this point, since they are quite mature.<br>
If you do feel the need, updating is a fairly simple process thanks to the included Uninstall function.

Here is what you need to do in order to update:

1. Backup your game's Mod Organizer 2 instance (`~/.local/share/proton-mo2-installer/modorganizer2/<chosen-game>`)
2. Run `setup`, following the prompts to *Uninstall*
3. Run `setup` again, following the prompts to *Install*
4. Copy the following files and directories from your backup to the fresh Mod Organizer 2 instance:
  - `downloads` directory
  - `mods` directory
  - `overwrite` directory
  - `ModOrganizer2.ini` file
  - `nxmhandler.ini` file


## Notes

- There is no Vortex support, and there probably never will be. In my experience, it simply isn't capable of handling heavy mod stacks nearly as well as Mod Organizer 2 is.


## Credits

- [Rockerbacon](https://github.com/rockerbacon) - Creating the original scripts that this project was reworked from.

    Nearly everything has been rewritten, save for the contents of `gamesinfo/` and `handlers/`.


## License

GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
