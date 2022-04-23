# Proton MO2 Installer
[![Latest Tag](https://img.shields.io/github/v/tag/ralgar/proton-mo2-installer?style=for-the-badge&logo=semver&logoColor=white)](https://github.com/ralgar/proton-mo2-installer/tags)
[![Software License](https://img.shields.io/github/license/ralgar/proton-mo2-installer?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Stars](https://img.shields.io/github/stars/ralgar/proton-mo2-installer?style=for-the-badge&logo=github&logoColor=white&color=gold)](https://github.com/ralgar/proton-mo2-installer)


## Overview
This project intends to make modding Bethesda games on Linux a reality for every Linux user. It provides a set of scripts, which automatically configure a fully functional modding setup.

**Note:** The only verified game at this time is Skyrim SE. I don't own the other games on PC.

### Features
- [x] Simple, GUI-driven installer. Installs, updates, and uninstalls cleanly.
- [x] Installs Mod Organizer 2, LOOT, and Script Extender
- [x] Launching the game from Steam now launches Mod Organizer 2 instead (see [Proton Shunt](https://github.com/ralgar/proton-shunt))
- [x] NXM links from your browser can be sent directly to Mod Organizer 2
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
3. Grab the latest stable release of the installer [here](https://github.com/ralgar/proton-mo2-installer/releases).
4. Run `setup`, and follow the prompts until finished.
5. Launch the game. It will now launch MO2 instead.

**Note:** Installing the Windows packages can take a long time in some cases. There is no fix for this, just be patient.


### Configuring Mod Organizer 2
**On the first run of MO2:**
- Choose *Create a portable instance*.
- Choose the game that you're installing for.
- Store the data in the default location, or anywhere else you like.
- Connect your Nexus account (using an API key is suggested).
- Click *Finish* to create the instance.
- Choose either *Yes* or *No* when asked if you want tutorials.
- Choose *Yes* when MO2 asks if you want it to handle NXM links.

**Executable Paths:**
- To regain access to the game's launcher, edit the executable path in MO2 by simply appending `.bak` to the filename.
- To add LOOT as an executable, the path is `Z:\home\my_user\.local\share\proton-mo2-installer\tools\loot\LOOT.exe`.

**Installing Additional Modding Tools:**
1. Install the tool as a mod, using MO2.
2. Under the `Data` tab, find the executable, right click it, and choose `Add as Executable`.


## Supported Games

The following is a small overview of the current state of each supported game:<br>
Note: Much of this data is carried over from [modorganizer2-linux-installer](https://github.com/rockerbacon/modorganizer2-linux-installer), and may be outdated.

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
If you do feel the need, updating is a painless process thanks to the installer's *Update* function.

Here is what you need to do in order to update:

1. Grab the latest stable release of the installer [here](https://github.com/ralgar/proton-mo2-installer/releases).
2. Run `setup`, following the prompts to *Update*.


## Notes

- There is no Vortex support, and there probably never will be. In my experience, it simply isn't capable of handling heavy mod stacks nearly as well as Mod Organizer 2 is.


## Credits

- [Rockerbacon](https://github.com/rockerbacon) - For creating the original scripts that inspired this project.

    The main `setup` script was written from scratch, the contents of `handlers/` have been heavily reworked, and the contents of `gamesinfo/` are mostly untouched.


## License

GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
