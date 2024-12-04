import unittest
from collections import OrderedDict
from decimal import Decimal
from jesth import box, errors
from jesth.section import Section
from jesth.converter import ValueConverter


TEXT_BODY = """\
# welcome
project = 'Jesth'
author = 'alex rustic'
pi = 3.141_592_653_589_793_238_46E0\
"""

DICT_BODY = OrderedDict([(box.CommentID(), box.Comment("# welcome")),
                         ("project", box.RawString("Jesth")),
                         ("author", box.RawString("alex rustic")),
                         ("pi", Decimal("3.141_592_653_589_793_238_46E0"))])


BASE_BODY = ["# welcome",
             "project = 'Jesth'",
             "author = 'alex rustic'",
             "pi = 3.141_592_653_589_793_238_46E0"]


class TestSectionClass(unittest.TestCase):

    def test_default_init(self):
        section = Section("header")
        self.assertEqual("header", section.header)
        self.assertEqual(list(), section.body)
        self.assertIsNotNone(section.value_converter)

    def test_init_with_dict_body(self):
        section = Section("header", DICT_BODY)
        r = section.body
        expected = BASE_BODY
        self.assertEqual(expected, r)

    def test_init_with_text_body(self):
        section = Section("header", TEXT_BODY)
        r = section.body
        expected = BASE_BODY
        self.assertEqual(expected, r)

    def test_init_with_base_body(self):
        section = Section("header", BASE_BODY)
        r = section.body
        expected = BASE_BODY
        self.assertEqual(expected, r)

    def test_init_with_custom_value_converter(self):
        value_converter = ValueConverter(float_decoder=Decimal)
        section = Section("", value_converter=value_converter)
        self.assertIs(Decimal, section.value_converter.float_decoder)

    def test_update_body(self):
        section = Section("header")
        invalid_base_body = 3.14
        with self.assertRaises(errors.ConversionError):
            # body should be a list of string, a dict, or a string
            section.update(invalid_base_body)

    def test_create_dict(self):
        # test with empty body
        section = Section("")
        r = section.create_dict()
        self.assertEqual(OrderedDict(), r)
        # empty body + default parameter set
        default = {"is_empty": True}
        r = section.create_dict(default)
        self.assertIs(default, r)
        # == test with existent and compatible body
        section.update(BASE_BODY)
        # compact_mode = true
        r = section.create_dict(strict=True)
        self.assertIsNotNone(r)
        self.assertFalse(_find_comment(r))
        # compact_mode = false
        r = section.create_dict(strict=False)
        self.assertIsNotNone(r)
        self.assertTrue(_find_comment(r))

    def test_create_dict_with_incompatible_body(self):
        section = Section("", ["hello world"])
        with self.assertRaises(Exception):
            section.create_dict()

    def test_to_text(self):
        # non-empty body
        section = Section("", ["hello", "world"])
        r = section.to_text()
        expected = "hello\nworld"
        self.assertEqual(expected, r)

    def test_to_text_with_empty_body(self):
        # empty body
        section = Section("")
        r = section.to_text()
        expected = ""
        self.assertEqual(expected, r)

    def test_to_dict(self):
        # test with empty body
        section = Section("")
        r = section.to_dict()
        self.assertEqual(OrderedDict(), r)
        # empty body + default parameter set
        default = {"is_empty": True}
        r = section.to_dict(default)
        self.assertIs(default, r)
        # == test with existent and compatible body
        section.update(BASE_BODY)
        # compact_mode = true
        r = section.to_dict(strict=True)
        self.assertIsNotNone(r)
        self.assertFalse(_find_comment(r))
        # compact_mode = false
        r = section.to_dict(strict=False)
        self.assertIsNotNone(r)
        self.assertTrue(_find_comment(r))

    def test_to_dict_with_incompatible_body(self):
        section = Section("", ["hello world"])
        fallback = {"something_wrong": True}
        r = section.to_dict(fallback=fallback)
        self.assertEqual(fallback, r)


def _find_comment(body, comment="# welcome"):
    for key, val in body.items():
        if val == comment:
            return True
    return False


if __name__ == '__main__':
    unittest.main()
