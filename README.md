# Open-Parsec-for-Linux

A Linux host compatible with Parsec clients, based on [Lowlat](https://github.com/nomi-san/lowlat).
The native application follows the layout of [OpenParsec for iPadOS](https://github.com/hugeBlack/OpenParsec): host cards, a top toolbar, bottom navigation and settings behind the gear button.

## Features

- Linux hosting with DRM/Vulkan capture and hardware H.264/HEVC encoding.
- Local computer card and live host status.
- Connected client list and session disconnection.
- Host name, codec, encoder, frame rate, bitrate and default display settings.
- GNOME panel indicator that remains active when the window is closed.
- GNOME Mutter resolution switching and remembered DING desktop file positions.

The host uses Parsec services. Other computers, friends and outgoing connections remain available in the official Parsec client. No mock computers are displayed. PipeWire capture, AV1 and special DING icons are not supported in this version.

## Quick install

Download the Linux x86_64 archive from this repository's Releases page, extract it and run:

```sh
./install.sh
```

The guided installer installs dependencies, asks you to sign in to Parsec, and enables automatic hosting plus a background panel indicator. Release archives include binaries, so no compiler is needed. The automatic installer targets Ubuntu 24.04–26.x; it is experimental and does not change GPU drivers or desktop login settings.

For verification, source builds, troubleshooting and removal, see [Installation](docs/INSTALL.md).

Administrative actions use a sudo terminal. Credentials stay outside the repository. Closing the window keeps the indicator active; quitting the interface leaves the host running.

## Development

```sh
python3 apps/control/desktop_app.py
python3 -m unittest discover -s tests/openparsec
```

Launch the optional web panel with `./open-parsec web --port 47990`. Local access requires the PIN displayed in the terminal. Machine-specific configurations, built binaries and credentials are excluded by `.gitignore`.

## Licenses and attribution

The host and Linux code are MIT-licensed; see [LICENSE](LICENSE) and [UPSTREAM.md](UPSTREAM.md).
The unchanged OpenParsec logo comes from the iPadOS project under GPL-3.0; see [its notice and license](apps/control/assets/NOTICE.md).
The GTK interface independently implements a similar layout; it contains no Swift source.
This project is independent of Parsec/Unity and the iPadOS client maintainers.

Use `python3 apps/control/desktop_app.py --background` for a panel-only launch. Opening the application launcher or choosing Show Open Parsec reveals the window.
