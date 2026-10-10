# Contributing

Please report reproducible bugs with Ubuntu version, desktop/session type (Wayland or X11), GPU and driver, archive version, expected behavior and actual behavior. Include only relevant, sanitized diagnostic output. Do not upload credentials, account responses, configuration directories or private screenshots.

The repository currently distributes source and binaries together in an archive. Documentation and packaging changes can be proposed directly here. Application changes must identify the affected source files inside the archive and describe how a replacement archive was built and tested. Do not label a binary as validated without testing it on the stated hardware.

Before a packaging change, run:

```sh
python3 scripts/verify_archive.py
python3 -m unittest discover -s tests
```

Update `SHA256SUMS` whenever the archive changes. Preserve upstream license notices and the logo's separate license. Packaging checks verify integrity and structure; they do not execute or validate the host, installer or streaming compatibility.

See [SECURITY.md](SECURITY.md) for vulnerability reports.
