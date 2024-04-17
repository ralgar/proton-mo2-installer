<!-- markdownlint-disable-next-line MD033 MD041 -->
<div align="center">

# Proton MO2 Installer

[![Latest Tag](https://img.shields.io/github/v/tag/ralgar/proton-mo2-installer?style=flat&label=Tag&logo=semver&logoColor=white)](https://github.com/ralgar/proton-mo2-installer/tags)
[![Software License](https://img.shields.io/github/license/ralgar/proton-mo2-installer?style=flat&label=License&logo=gnu&logoColor=white)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Stars](https://img.shields.io/github/stars/ralgar/proton-mo2-installer?style=flat&label=Stars&logo=github&logoColor=white&color=gold)](https://github.com/ralgar/proton-mo2-installer)

</div>

## Overview

This project intends to make modding Bethesda games a breeze for Linux users. It provides a set of scripts, which automatically configure a ready-to-use modding environment for the game.

There is also a [wiki](https://github.com/ralgar/proton-mo2-installer/wiki) to document the installation and usage of other tools.

### Features

- [x] Simple, GUI-driven installer, written in Bash. Installs, updates, and uninstalls cleanly.
- [x] Installs Mod Organizer 2 with integrated LOOT.
- [x] Installs the Script Extender for the chosen game.
- [x] Launching the game from Steam launches Mod Organizer 2 instead (uses [Proton Shunt](https://github.com/ralgar/proton-shunt)).
- [x] NXM links from your browser will be sent to Mod Organizer 2.
- [x] DynDOLOD, FNIS, Nemesis, BodySlide, Outfit Studio, and other tools all work as expected. See the [wiki](https://github.com/ralgar/proton-mo2-installer/wiki) for details.
- [ ] Steam Deck support - I don't own one, but I believe it should work. Please [open an issue](https://github.com/ralgar/proton-mo2-installer/issues) if it doesn't.
- [ ] Flatpak Steam support - Currently unsupported. Contributions welcome.

## Getting Started

### Prerequisites

You may need to install the following dependencies:

- bsdtar
- curl
- protontricks
- xdg-utils
- zenity

### Installation

Installation is simple:

1. Install your chosen game through Steam.
2. Grab the latest stable release of the installer [here](https://github.com/ralgar/proton-mo2-installer/releases).
3. Run `setup`, and follow the prompts until finished.
4. Launch the game via Steam. It will now launch MO2 instead.

**Notes:**

- The installer may interact with Steam in various ways, this may include
  closing running Steam instances, and launching the game to inititalize the
  prefix if needed. Do NOT interfere with this process or the installation
  will fail to complete.

### Configuring Mod Organizer 2

**On the first run of MO2:**

- Choose *Create a portable instance*.
- Choose the game that you're installing for.
- You can store your instance data in the default location, or anywhere else you like.
- Connect your Nexus account (using an API key is recommended).
- Click *Finish* to create the instance.
- Choose either *Yes* or *No* when asked if you want tutorials.
- Choose *Yes* when MO2 asks if you want it to handle NXM links.

**Executable Paths:**

- To regain access to the game's launcher, edit the executable path in MO2, appending `.bak` to the filename.

#### Installing Additional Modding Tools

Most tools can simply be installed via MO2. See the [wiki](https://github.com/ralgar/proton-mo2-installer/wiki).

LOOT is already integrated with MO2, just press the *Sort* button under the *Plugins* tab.

## Supported Games

The following is a small overview of the current state of each supported game.

|                          | GAMEPLAY        | SCRIPT EXTENDER |
| ------------------------ | --------------- | --------------- |
| **Fallout 3**            | Untested        | Untested        |
| **Fallout 4**            | Working         | Working         |
| **Fallout: New Vegas**   | Untested        | Untested        |
| **Morrowind**            | Untested        | Untested        |
| **Oblivion**             | Untested        | Untested        |
| **Skyrim**               | Untested        | Untested        |
| **Skyrim SE/AE (v1.6+)** | Working         | Working         |

For known bugs and workarounds, please refer to the [issues page](https://github.com/ralgar/proton-mo2-installer/issues?q=is:issue+is:open+label:bug+)

Please help to keep this table up to date by [opening issues](https://github.com/ralgar/proton-mo2-installer/issues/new/choose) with any problems you encounter.

**NOTE:** The recommended Proton version is currently official Proton 8.0.

## Updating

Updating is a painless process thanks to the installer's *Update* function.

Here is what you need to do in order to update:

1. Grab the latest stable release of the installer [here](https://github.com/ralgar/proton-mo2-installer/releases).
1. Make sure Steam is *not* running before starting the installer.
1. Run `setup`, following the prompts to *Update*.

## Uninstalling

Uninstalling is simple, just run `setup`, and follow the prompts to uninstall.

**Note:** The uninstaller will *never* remove the `~/.local/share/proton-mo2-installer` directory. Because this is the default location for MO2 instances, some users may have mods stored in this location. To prevent any accidental data loss, it is up to you to remove this directory manually.

## Acknowledgements

- [Rockerbacon](https://github.com/rockerbacon) - For creating the original
  Lutris scripts that inspired this project. All code is my own, but following
  Rockerbacon's methods for managing MO2.

## License

GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
