import unittest
import tempfile
import pathlib
from decimal import Decimal
from jesth import Parser, parse, read
from jesth.converter import ValueConverter


TEXT = """\
Anonymous
section
here.

[section2]
hello
\\[world
"""


TEXT_WITH_END = """\
[section1]
first
section

[[END]]

[section2]
second
section
"""


class TestReadFunc(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(TEXT.encode("utf-8"))
        file.close()
        self._path_str = file.name
        self._path_obj = pathlib.Path(self._path_str)

    def tearDown(self):
        self._path_obj.unlink()

    def test_read_from_file(self):
        with open(self._path_str, mode="rb") as file:
            document = read(file)
        test_document(document, self)

    def test_read_from_path_str(self):
        document = read(self._path_str)
        test_document(document, self)

    def test_read_from_path_obj(self):
        document = read(self._path_obj)
        test_document(document, self)

    def test_read_with_custom_value_converter(self):
        custom_float_decoder = Decimal
        custom_value_converter = ValueConverter(float_decoder=custom_float_decoder)
        document = read(self._path_obj, value_converter=custom_value_converter)
        section1 = document.sections[0]
        section2 = document.sections[1]
        expected = custom_float_decoder
        self.assertEqual(expected, section1.value_converter.float_decoder)
        self.assertEqual(expected, section2.value_converter.float_decoder)


class TestParseFunc(unittest.TestCase):

    def test_with_default_args(self):
        document = parse(TEXT)
        test_document(document, self)

    def test_with_custom_value_converter(self):
        custom_float_decoder = Decimal
        custom_value_converter = ValueConverter(float_decoder=custom_float_decoder)
        document = parse(TEXT, value_converter=custom_value_converter)
        section1 = document.sections[0]
        section2 = document.sections[1]
        expected = custom_float_decoder
        self.assertEqual(expected, section1.value_converter.float_decoder)
        self.assertEqual(expected, section2.value_converter.float_decoder)


class TestParserClass(unittest.TestCase):

    def test(self):
        parser = Parser()
        self.assertTrue(parser.feedable)
        for line in TEXT_WITH_END.split("\n"):
            parser.feed(line)
            if line.lower() == "[[end]]":
                self.assertFalse(parser.feedable)
        self.assertEqual(1, len(parser.sections))


def test_document(document, test_case):
    test_case.assertEqual(2, len(document.sections))
    section1, section2 = document.sections
    # section1
    expected_header = ""
    expected_body = ["Anonymous", "section", "here."]
    test_case.assertEqual(expected_header, section1.header)
    test_case.assertEqual(expected_body, section1.body)
    # section2
    expected_header = "section2"
    expected_body = ["hello", "[world"]
    test_case.assertEqual(expected_header, section2.header)
    test_case.assertEqual(expected_body, section2.body)


if __name__ == "__main__":
    unittest.main()
