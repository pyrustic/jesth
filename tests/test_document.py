import unittest
import tempfile
import pathlib
from decimal import Decimal
from jesth import parse, read, ValueConverter


RAW_DOCUMENT = """\
Top anonymous
section

[user]
id = 1
name = 'alex'

[info]
project = 'jesth'
repository = 'https://github.com/pyrustic/jesth'

[user]
id = 2
name = 'rustic'\
"""


USER_AND_INFO = """\
[user]
id = 1
name = 'alex'

[info]
project = 'jesth'
repository = 'https://github.com/pyrustic/jesth'

[user]
id = 2
name = 'rustic'\
"""


USER_ONLY = """\
[user]
id = 1
name = 'alex'


[user]
id = 2
name = 'rustic'\
"""


class TestDocumentCreationWithParseFunc(unittest.TestCase):

    def test_with_default_args(self):
        document = parse(RAW_DOCUMENT)
        expected_headers = {"", "user", "info"}
        self.assertEqual(expected_headers, document.headers)
        self.assertIsNotNone(document.value_converter)
        self.assertEqual(4, len(document.sections))

    def test_with_custom_value_converter(self):
        value_converter = ValueConverter(float_decoder=Decimal)
        document = parse(RAW_DOCUMENT, value_converter=value_converter)
        self.assertIs(Decimal, document.value_converter.float_decoder)


class TestFileBasedDocument(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(RAW_DOCUMENT.encode("utf-8"))
        file.close()
        self._path_str = file.name
        self._path_obj = pathlib.Path(self._path_str)

    def tearDown(self):
        self._path_obj.unlink()

    def test_document_creation_with_read_func(self):
        # create temporary file
        document = read(self._path_str)
        expected_headers = {"", "user", "info"}
        self.assertEqual(expected_headers, document.headers)
        self.assertIsNotNone(document.value_converter)
        self.assertEqual(self._path_str, document.path)
        # with custom ValueConverter
        value_converter = ValueConverter(float_decoder=Decimal)
        document = read(self._path_str, value_converter=value_converter)
        self.assertIs(Decimal, document.value_converter.float_decoder)

    def test_save_method(self):
        document = read(self._path_str)
        document.append("new_header")
        r = document.save()
        self.assertTrue(r)
        # check
        with open(self._path_str, "r") as file:
            data = file.read()
        expected = RAW_DOCUMENT + "\n\n[new_header]"
        self.assertEqual(expected, data)


class TestDocumentCloning(unittest.TestCase):

    def setUp(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        file.close()
        self._path_str = file.name
        self._path_obj = pathlib.Path(self._path_str)

    def tearDown(self):
        self._path_obj.unlink()

    def test_save_to_method(self):
        document = parse(RAW_DOCUMENT)
        document.save_to(self._path_str)
        # check
        with open(self._path_str, "r") as file:
            data = file.read()
        self.assertEqual(data, RAW_DOCUMENT)


class TestDocumentRenderMethod(unittest.TestCase):

    def test_render_all_doc(self):
        document = parse(RAW_DOCUMENT)
        # render all doc
        r = document.render()
        expected = RAW_DOCUMENT
        self.assertEqual(expected, r)

    def test_render_specific_section(self):
        document = parse(RAW_DOCUMENT)
        # render specific section
        r = document.render("user", spacing=2)
        expected = USER_ONLY
        self.assertEqual(expected, r)

    def test_render_selected_sections(self):
        document = parse(RAW_DOCUMENT)
        # render specific sections
        r = document.render("user", "info", spacing=1)
        expected = USER_AND_INFO
        self.assertEqual(expected, r)
        # render specific sections
        r = document.render("", "info", "user")
        expected = RAW_DOCUMENT
        self.assertEqual(expected, r)


class TestDocumentDataInsertionMethods(unittest.TestCase):

    def test_set_section_at_begin(self):
        text = "[section1]\n\n[section2]"
        # insert at begin
        document = parse(text)
        document.set(0, "new_section")
        expected = "[new_section]\n\n[section2]"
        self.assertEqual(expected, document.render())

    def test_set_section_at_end(self):
        text = "[section1]\n\n[section2]"
        # insert at the end
        document = parse(text)
        document.set(-1, "new_section")
        expected = "[section1]\n\n[new_section]"
        self.assertEqual(expected, document.render())

    def test_insert_at_begin(self):
        text = "[section1]\n\n[section2]"
        # insert at 0
        document = parse(text)
        document.insert(0, "new_section")
        expected = "[new_section]\n\n" + text
        self.assertEqual(expected, document.render())

    def test_insert_at_end(self):
        text = "[section1]\n\n[section2]"
        # insert at the end
        document = parse(text)
        document.insert(2, "new_section")
        expected = text + "\n\n[new_section]"
        self.assertEqual(expected, document.render())

    def test_insert_at_middle(self):
        text = "[section1]\n\n[section2]"
        # insert at the middle
        document = parse(text)
        document.insert(1, "new_section")
        expected = "[section1]\n\n[new_section]\n\n[section2]"
        self.assertEqual(expected, document.render())

    def test_append_method(self):
        document = parse(USER_ONLY)
        document.append("new_section")
        expected = USER_ONLY + "\n\n\n[new_section]"
        self.assertEqual(expected, document.render(spacing=2))


class TestDocumentDataRetrivalMethods(unittest.TestCase):

    def test_get_method(self):
        # default
        document = parse(USER_ONLY)
        user = document.get("user")
        expected_body = ["id = 1", "name = 'alex'"]
        self.assertEqual(expected_body, user.body)
        # specific index
        user = document.get("user", 1)
        expected_body = ["id = 2", "name = 'rustic'"]
        self.assertEqual(expected_body, user.body)
        # specific index
        user = document.get("user", -1)
        expected_body = ["id = 2", "name = 'rustic'"]
        self.assertEqual(expected_body, user.body)

    def test_get_all_method(self):
        document = parse(USER_ONLY)
        users = document.get_all("user")
        expected_bodies = (["id = 1", "name = 'alex'"],
                           ["id = 2", "name = 'rustic'"])
        for i, user in enumerate(users):
            self.assertEqual(expected_bodies[i], user.body)

    def test_count_method(self):
        document = parse(USER_ONLY)
        self.assertEqual(2, document.count("user"))


class TestDocumentDataSuppressionMethods(unittest.TestCase):

    def test_remove_section_with_default_args(self):
        document = parse(USER_ONLY)
        self.assertEqual(2, document.count("user"))
        document.remove("user")
        user = document.get("user")
        expected_body = ["id = 1", "name = 'alex'"]
        self.assertEqual(expected_body, user.body)
        self.assertEqual(1, document.count("user"))
        self.assertEqual(1, count_sections(document, "user"))

    def test_remove_section_at_relative_index(self):
        # remove first item
        document = parse(USER_ONLY)
        self.assertEqual(2, document.count("user"))
        document.remove("user", 0)
        user = document.get("user")
        expected_body = ["id = 2", "name = 'rustic'"]
        self.assertEqual(expected_body, user.body)
        self.assertEqual(1, document.count("user"))
        self.assertEqual(1, count_sections(document, "user"))
        # remove second item
        document = parse(USER_ONLY)
        document.remove("user", 1)
        user = document.get("user")
        expected_body = ["id = 1", "name = 'alex'"]
        self.assertEqual(expected_body, user.body)
        self.assertEqual(1, document.count("user"))
        self.assertEqual(1, count_sections(document, "user"))

    def test_remove_all_method(self):
        document = parse(USER_AND_INFO)
        self.assertEqual(2, document.count("user"))
        self.assertEqual(2, count_sections(document, "user"))
        self.assertEqual(1, document.count("info"))
        self.assertEqual(1, count_sections(document, "info"))
        document.remove_all("user")
        self.assertEqual(0, document.count("user"))
        self.assertEqual(0, count_sections(document, "user"))
        self.assertEqual(1, document.count("info"))
        self.assertEqual(1, count_sections(document, "info"))


def count_sections(document, header):
    """Count sections in a document with a specific header"""
    i = 0
    for s in document.sections:
        if s.header == header:
            i += 1
    return i


if __name__ == '__main__':
    unittest.main()
