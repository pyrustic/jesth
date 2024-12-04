import unittest
import tempfile
import pathlib
from jesth.parser import parse
from jesth.renderer import render, write


TEXT = """\
[section1]
first
section


[section2]
second
section\
"""


class TestRenderFunc(unittest.TestCase):

    def test_render_all_sections(self):
        document = parse(TEXT)
        r = render(document, spacing=2)
        expected = TEXT
        self.assertEqual(expected, r)

    def test_render_only_one_section(self):
        document = parse(TEXT)
        r = render(document, "section2")
        expected = "[section2]\nsecond\nsection"
        self.assertEqual(expected, r)


class TestWriteFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path_str = file.name
        self._path_obj = pathlib.Path(self._path_str)
        self._document = parse(TEXT)

    def tearDown(self):
        self._path_obj.unlink()

    def test_write_to_path_obj(self):
        expected = write(self._document, self._path_obj)
        _check_file_contents(self, self._path_str, expected)

    def test_write_to_path_str(self):
        expected = write(self._document, self._path_str)
        _check_file_contents(self, self._path_str, expected)

    def test_write_to_file(self):
        with open(self._path_str, "wb") as file:
            expected = write(self._document, file)
        _check_file_contents(self, self._path_str, expected)


def _check_file_contents(test_case, path_str, expected_contents):
    with open(path_str, "r") as file:
        contents = file.read()
        test_case.assertEqual(expected_contents, contents)


if __name__ == '__main__':
    unittest.main()
