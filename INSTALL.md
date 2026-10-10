# Installation and troubleshooting

Follow the [README](../README.md#install) to download and verify the archive. Run installer commands from the extracted `open-parsec-0.1.0` directory, as a normal user in an active graphical session.

## Before installing

```sh
./install.sh --check
```

This check reports platform and bundled-binary availability without installing dependencies or changing services. It is not a full GPU or streaming test. The installer requires Ubuntu 24.04–26.x, x86_64, sudo, apt, systemd, Python 3 and a desktop D-Bus session. Other distributions need manual adaptation.

The installation uses system-wide paths and sudo: it installs packages and helpers, stores host configuration under `/etc/openparsec`, enables `open-parsecd.service`, and adds a per-user session service and desktop integration. Sign-in happens in a terminal. Do not run the complete installer as root or from a headless SSH session.

Keep your existing GPU drivers. Vulkan and hardware encoding must work on the host. GNOME display-mode integration relies on Mutter; custom EDID installation is outside this guide. Remote access still depends on the host being awake and network connectivity.

## Diagnose without changing configuration

```sh
systemctl status open-parsecd.service --no-pager
systemctl --user status open-parsec-session.service --no-pager
open-parsec doctor
```

For recent service messages:

```sh
journalctl -u open-parsecd.service -n 100 --no-pager
journalctl --user -u open-parsec-session.service -n 100 --no-pager
```

Inspect output locally before sharing: remove tokens, account details, hostnames, IP addresses and personal paths. Never upload `/etc/openparsec/session.env` or an unfiltered configuration directory.

If sign-in expired, rerun `sudo open-parsec-login --install` from a terminal. This changes saved authentication; only do it when authentication is the problem. If the panel closes but hosting continues, that is expected: the service runs separately from the interface.

## Remove the application

These commands modify the installation. Run them from the extracted archive only when you intend to uninstall:

```sh
sudo sh scripts/uninstall-openparsec.sh
systemctl --user disable --now open-parsec-session.service
rm -f ~/.config/autostart/org.openparsec.Desktop.desktop
```

Configuration and authentication files may remain under `/etc/openparsec` and `~/.config/openparsec`. Review them before removing them separately. Uninstalling the application does not revoke a session on Parsec's servers.

## Source builds

Source is included in the archive. Read its `README.lowlat.md`, `Cargo.toml`, `rust-toolchain.toml` and `scripts/build-openparsec.sh` before building. A source build needs Rust and native build dependencies; the bundled binary installation does not.
