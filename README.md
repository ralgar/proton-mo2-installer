# Mod Tools Installer Framework
[![Latest Tag](https://img.shields.io/github/v/tag/ralgar/proton-mo2-installer?style=for-the-badge&logo=semver&logoColor=white)](https://github.com/ralgar/proton-mo2-installer/tags)
[![Software License](https://img.shields.io/github/license/ralgar/proton-mo2-installer?style=for-the-badge&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Stars](https://img.shields.io/github/stars/ralgar/proton-mo2-installer?style=for-the-badge&logo=github&logoColor=white&color=gold)](https://github.com/ralgar/proton-mo2-installer)


## Overview
A framework for automating the installation of modding tools on Linux. It
 currently has full support for Proton (Steam Play for Linux), and Bethesda
 games, where it is capable of delivering an advanced, turn-key modding setup
 using Mod Organizer 2, and other tools.

Due to the modular nature of the project, adding support for new games, or
 modding tools, is as simple as writing a new module. See `CONTRIBUTING.md`
 for more information on how you can help.

There is also a [wiki](https://github.com/ralgar/proton-mo2-installer/wiki) to document the installation, usage, and troubleshooting of other tools.

### Features
- [x] Simple, TUI-driven installer. Installs, updates, and uninstalls cleanly.
- [x] Installs Mod Organizer 2 with integrated LOOT.
- [x] Installs the Script Extender for the chosen game.
- [x] Installs custom Proton version required for Mod Organzer 2.
- [x] Launching the game from Steam now launches Mod Organizer 2 instead (uses [Proton Shunt](https://github.com/ralgar/proton-shunt)).
- [x] NXM links from your browser will be sent directly to Mod Organizer 2.
- [x] DynDOLOD, FNIS, Nemesis, BodySlide, Outfit Studio, and other tools all work as expected. See the [wiki](https://github.com/ralgar/proton-mo2-installer/wiki) for details.
- [x] Flatpak Steam support
- [x] Steam Deck support


## Getting Started

### Install using pip

**Prerequisites:**
- python >= 3.7
- pip

**Installation:**

```sh
pip install pmf
```

### Usage

Just run `pmf` from the command line. Follow the TUI from there

### Configuring Mod Organizer 2
**On the first run of MO2:**
- Choose *Create a portable instance*.
- Choose the game that you're installing for.
- Store your instance data in the default location, or anywhere else you like.
- Connect your Nexus account (using an API key is recommended).
- Click *Finish* to create the instance.
- Choose either *Yes* or *No* when asked if you want tutorials.
- Choose *Yes* when MO2 asks if you want it to handle NXM links.

**Executable Paths:**
- To regain access to the game's launcher, edit the executable path in MO2 by simply appending `.bak` to the filename.

**Installing Additional Modding Tools:**
See the [wiki](https://github.com/ralgar/proton-mo2-installer/wiki).

**Note:** LOOT is included in MO2, just press the *Sort* button under the *Plugins* tab.


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

Updating is a painless process thanks to the installer's *Update* function.

Here is what you need to do in order to update:

1. Grab the latest stable release of the installer [here](https://github.com/ralgar/proton-mo2-installer/releases).
2. Make sure Steam is *not* running before starting the installer.
3. Run `pmf`, following the prompts to *Update*.


## Uninstalling

Uninstalling is simple, just run `pmf`, and follow the prompts to uninstall.

**Note:** The uninstaller will *never* remove the `~/.local/share/proton-mo2-installer` directory. Because this is the default location for MO2 instances, some users may have mods stored in this location. To prevent any accidental data loss, it is up to you to remove this directory manually.


## Credits

- [Rockerbacon](https://github.com/rockerbacon) - For creating the original Lutris scripts that inspired this project.
- [Frostworx](https://github.com/frostworx) - For building the custom version of Proton, required to run Mod Organizer 2 smoothly.


## License

GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
