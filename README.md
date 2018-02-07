# The FSMI status display
Displays stuff on screens. Driven by simple (or sometimes not so simple)
plugins, most of which just output to `stdout`.

Also allows playing games, streaming video and other useful things on the big
screen.

## How does it work
Basically by scripting a tiling window manager (`ratpoison`) using a window-manager-manager
(`rpcd`), which also provides a client-facing API and a web interface for starting things.

Most standard windows are [`xecho`](https://github.com/cbdevnet/xecho) instances fed from
stdin using bash scripts.

`rpcd` provides tools for automatically swapping windows on the display using an API,
which is used by a watchdog script to react to external events.

In some places, this repository contains references to files in the `non-public/` directory,
which is not provided to the general public for various reasons.

## Building
* Clone this repository including the submodules
* Install all prerequisites
* Run make in the `tooling/` directory

## Usage
* Make sure one (or more) X servers are running
* Start the display using the `./statusdisplay` script

## Contents of this repository

* `sd-config`: Contains per-host configuration for the display
* `statusdisplay`: Launch script
* `control/`: Control facilities for various commands, including `rpcd`
* `config/`: Configuration files for commands & windows
* `layouts/`: Display layouts used for ratpoison
* `logs/`: Used for log files
* `non-public`: Privileged configuration files and tools
* `scripts/`: Scripts used for providing user-startable commands
* `tooling/`: Tools used for the operation of this repository, most provided as git submodules
* `windows/`: Scripts used for providing automated information windows

## License
All code within this repository itself is placed under the BSD 2-clause license, as reproduced
in [LICENSE.txt](LICENSE.txt). The various third-party repositories in `tooling/` impose their
own respective licenses.
