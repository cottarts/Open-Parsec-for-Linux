"""Check the distribution without extracting or executing its contents."""
import hashlib
from pathlib import Path, PurePosixPath
import re
import tarfile

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'install.sh', 'LICENSE', 'UPSTREAM.md', 'Cargo.toml',
            'apps/control/desktop_app.py', 'scripts/install-openparsec.sh',
            'scripts/uninstall-openparsec.sh', 'bin/open-parsecd',
            'apps/control/assets/NOTICE.md', 'apps/control/assets/LICENSE.GPL-3.0'}


def validate_members(members):
    names = set()
    roots = set()
    for member in members:
        path = PurePosixPath(member.name)
        if path.is_absolute() or '..' in path.parts or not path.parts:
            raise ValueError(f'Unsafe archive path: {member.name}')
        # No links or device nodes are needed by this distribution.
        if not (member.isfile() or member.isdir()):
            raise ValueError(f'Unsupported archive entry: {member.name}')
        if member.name in names:
            raise ValueError(f'Duplicate archive entry: {member.name}')
        names.add(member.name)
        roots.add(path.parts[0])
    if len(roots) != 1:
        raise ValueError('Expected one top-level distribution directory')
    root = roots.pop()
    missing = REQUIRED - {str(PurePosixPath(n).relative_to(root)) for n in names}
    if missing:
        raise ValueError('Missing required files: ' + ', '.join(sorted(missing)))
    return root


def verify(root=ROOT):
    lines = (root / 'SHA256SUMS').read_text().splitlines()
    if len(lines) != 1:
        raise ValueError('Expected one archive checksum')
    match = re.fullmatch(r'([0-9a-f]{64})  (open-parsec-[\w.\-]+\.tar\.gz)', lines[0])
    if not match:
        raise ValueError('Invalid checksum entry')
    expected, filename = match.groups()
    archive = root / filename
    with archive.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    if digest != expected:
        raise ValueError('Archive checksum mismatch')
    with tarfile.open(archive, 'r:gz') as stream:
        directory = validate_members(stream.getmembers())
    print(f'OK: SHA-256 and archive layout verified ({filename}, {directory})')


if __name__ == '__main__':
    verify()
