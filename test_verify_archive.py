import importlib.util
from pathlib import Path
import tarfile
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('verify_archive', Path(__file__).resolve().parents[1] / 'scripts/verify_archive.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def member(name, kind=tarfile.REGTYPE):
    entry = tarfile.TarInfo(name)
    entry.type = kind
    return entry


class ArchiveSafetyTests(unittest.TestCase):
    def valid_members(self):
        return [member('release/' + name) for name in module.REQUIRED]

    def test_valid_layout(self):
        self.assertEqual(module.validate_members(self.valid_members()), 'release')

    def test_rejects_traversal_and_absolute_paths(self):
        for path in ['/etc/file', 'release/../../file']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                module.validate_members(self.valid_members() + [member(path)])

    def test_rejects_links_and_devices(self):
        for kind in [tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.CHRTYPE]:
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                module.validate_members(self.valid_members() + [member('release/link', kind)])

    def test_rejects_duplicate_entries(self):
        entries = self.valid_members()
        with self.assertRaises(ValueError):
            module.validate_members(entries + [entries[0]])

    def test_rejects_missing_files(self):
        with self.assertRaises(ValueError):
            module.validate_members([member('release/LICENSE')])

    def test_rejects_multiple_roots(self):
        with self.assertRaises(ValueError):
            module.validate_members(self.valid_members() + [member('other/file')])

    def test_rejects_checksum_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'SHA256SUMS').write_text('0' * 64 + '  open-parsec-test.tar.gz\n')
            (root / 'open-parsec-test.tar.gz').write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError, 'checksum mismatch'):
                module.verify(root)


if __name__ == '__main__':
    unittest.main()
