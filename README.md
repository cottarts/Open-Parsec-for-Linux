# Open Parsec for Linux

An experimental Linux host for Parsec clients, based on [Lowlat](https://github.com/nomi-san/lowlat). Includes a native GTK control panel inspired by [OpenParsec for iPadOS](https://github.com/hugeBlack/OpenParsec).

## What it does

- Capture the desktop through DRM/Vulkan and encode with hardware H.264 or HEVC.
- Show the local host, live status and connected clients; disconnect sessions.
- Configure host name, encoder, codec, frame rate, bitrate and display settings.
- Keep a GNOME panel indicator available when the window closes.
- Switch resolution through GNOME Mutter and remember DING desktop file positions.

This version uses Parsec services and requires a Parsec account. Use the official client for outgoing connections, friends and other computers. PipeWire capture, AV1 and special DING icons are not supported.

## Install

The guided installer targets **Ubuntu 24.04–26.x on x86_64**, with a graphical session and systemd. GPU drivers must already provide Vulkan and a supported hardware encoder. This is experimental: the installer accepts these Ubuntu versions, but that does not establish compatibility with every GPU or desktop combination.

1. Download the [0.1.0 archive](https://github.com/cottarts/Open-Parsec-for-Linux/raw/refs/heads/main/open-parsec-0.1.0-linux-x86_64.tar.gz) and [SHA256SUMS](SHA256SUMS) into the same directory.
2. Verify, extract and check the platform:

```sh
sha256sum -c SHA256SUMS
tar -xzf open-parsec-0.1.0-linux-x86_64.tar.gz
cd open-parsec-0.1.0
./install.sh --check
```

3. From a terminal in your desktop session, run `./install.sh` as your normal user. It asks for sudo when needed, installs dependencies, guides Parsec sign-in and enables the host service and session interface. Binaries are included; a Rust compiler is not required for this archive.

The checksum detects changes or download corruption; it is not an independent proof of publisher identity. The installer does not replace GPU drivers or enable desktop auto-login.

See [installation and troubleshooting](docs/INSTALL.md) before installation, and [security guidance](SECURITY.md) before sharing logs.

## Use and develop

Closing the interface keeps its indicator active. Quitting the interface leaves the host service running. Use the launcher or the indicator's **Show Open Parsec** action to reopen the window.

**This repository distributes an archive.** The application source, bundled binaries and upstream documentation are inside it; cloning this repository alone does not create an application source checkout. After extracting, run these commands from `open-parsec-0.1.0`:

```sh
python3 apps/control/desktop_app.py
python3 -m unittest discover -s tests/openparsec
```

For a panel-only launch, add `--background`. The optional local web panel starts with `./open-parsec web --port 47990` and requires its terminal PIN. Read the archive's `README.lowlat.md` and `docs/` for architecture and source-build details.

Repository packaging checks, requiring only Python 3:

```sh
python3 scripts/verify_archive.py
python3 -m unittest discover -s tests
```

See [contributing](CONTRIBUTING.md) for safe reports and packaging changes.

## Licenses

Host and Linux application code: [MIT](LICENSE), with [upstream attribution and pinned commit](UPSTREAM.md). The unchanged iPadOS OpenParsec logo has a separate [GPL-3.0 notice](docs/LOGO-NOTICE.md) and [license](docs/LICENSE.GPL-3.0). The GTK interface contains no Swift source.

This project is independent of Parsec/Unity, Lowlat and the iPadOS client maintainers. Compatibility with Parsec services is not guaranteed.
