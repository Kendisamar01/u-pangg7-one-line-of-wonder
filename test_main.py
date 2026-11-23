import tempfile
import unittest
from pathlib import Path

import main


class EntryTests(unittest.TestCase):
    def test_write_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = main.write_entry(Path(tmp))
            data = path.read_bytes()
            self.assertEqual(data, main.ENTRY.encode("utf-8"))
            self.assertEqual(data.decode("utf-8"), main.ENTRY)
            self.assertTrue(1 <= len(main.ENTRY) <= 200)
            self.assertNotIn(b"\n", data)

    def test_rejects_bad_entries(self):
        bad_entries = ("", " \t ", "x" * 201, "line\nbreak", "\ud800")
        for bad in bad_entries:
            with self.subTest(bad=repr(bad)):
                with self.assertRaises(ValueError):
                    main.validate_entry(bad)


if __name__ == "__main__":
    unittest.main()
