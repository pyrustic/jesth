import unittest
import os.path
import tempfile
from jesth import misc, errors, const
from jesth.section import Section


class TestEnsureParentDirFunc(unittest.TestCase):

    def setUp(self):
        self._temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._temp_dir.cleanup()

    def test(self):
        path1 = os.path.join(self._temp_dir.name, "sub", "dir")
        path2 = os.path.join(path1, "file.txt")
        self.assertEqual(False, os.path.isdir(path1))
        misc.ensure_parent_dir(path2)
        self.assertEqual(True, os.path.isdir(path1))


class TestSplitValueFunc(unittest.TestCase):

    def test_with_default_args(self):
        line = " key = 'value here' "
        r = misc.split_key_value(line)
        expected = ("key", "'value here'")
        self.assertEqual(expected, r)

    def test_with_whitespace_stripping_disabled(self):
        line = " key = 'value here' "
        r = misc.split_key_value(line, strip_whitespace=False)
        expected = (" key ", " 'value here' ")
        self.assertEqual(expected, r)

    def test_with_colon_as_separator(self):
        line = " key : 'value here' "
        r = misc.split_key_value(line, sep=":")
        expected = ("key", "'value here'")
        self.assertEqual(expected, r)


class TestCorrectIndexFunc(unittest.TestCase):

    def test_with_positive_index(self):
        # correct index
        size = 5
        for i in range(size):
            r = misc.correct_index(index=i, size=size)
            expected = i
            self.assertEqual(expected, r)
        # out of bound index
        r = misc.correct_index(index=7, size=6)
        expected = 5
        self.assertEqual(expected, r)
        # out of bound index + ignore upper bound
        r = misc.correct_index(index=7, size=6, ignore_upper_bound=True)
        expected = 7
        self.assertEqual(expected, r)

    def test_with_negative_index(self):
        # correct index
        size = 5
        expected = 0
        for i in range(-size, 0):
            r = misc.correct_index(index=i, size=size)
            self.assertEqual(expected, r)
            expected += 1
        # out of bound index
        r = misc.correct_index(index=-7, size=6)
        expected = 0
        self.assertEqual(expected, r)

"""
class TestUpdateCachedRefsFunc(unittest.TestCase):

    def test(self):
        cached_refs = list()
        misc.update_cached_refs(1, cached_refs)
        self.assertEqual(1, len(cached_refs))
        with self.assertRaises(errors.Error):
            misc.update_cached_refs(1, cached_refs)
"""

class TestCountIndentsFunc(unittest.TestCase):

    def test_with_valid_indent(self):
        indent = " " * const.INDENT_WIDTH
        hello_world = "Hello World !"
        line = indent + indent + hello_world
        r = misc.count_indents(line)
        expected = 2
        self.assertEqual(expected, r)

    def test_with_invalid_indent(self):
        indent = " " * (const.INDENT_WIDTH + 1)
        hello_world = "Hello World !"
        line = indent + indent + hello_world
        with self.assertRaises(errors.IndentError):
            misc.count_indents(line)


class TestCleanLeadingBackslashesFunc(unittest.TestCase):

    def test_trivial_line(self):
        leading_backslash = "\\"
        line1 = "Hello World !"
        line2 = leading_backslash + line1
        r = misc.clean_leading_backslashes(line2)
        expected = leading_backslash + line1
        self.assertEqual(expected, r)

    def test_line_without_leading_backslash(self):
        line = "[Hello World !"
        r = misc.clean_leading_backslashes(line)
        expected = line
        self.assertEqual(expected, r)

    def test_line_with_one_leading_backslash(self):
        leading_backslash = "\\"
        line1 = "[Hello World !"
        line2 = leading_backslash + line1
        r = misc.clean_leading_backslashes(line2)
        expected = line1
        self.assertEqual(expected, r)

    def test_line_with_two_leading_backslash(self):
        leading_backslash = "\\"
        line1 = "[Hello World !"
        line2 = leading_backslash + leading_backslash + line1
        r = misc.clean_leading_backslashes(line2)
        expected = leading_backslash + line1
        self.assertEqual(expected, r)

    def test_line_with_three_leading_backslash(self):
        leading_backslash = "\\"
        line1 = "[Hello World !"
        line2 = leading_backslash + leading_backslash + leading_backslash + line1
        r = misc.clean_leading_backslashes(line2)
        expected = leading_backslash + leading_backslash + line1
        self.assertEqual(expected, r)


class TestAddLeadingBackslashesFunc(unittest.TestCase):

    def test_trivial_line(self):
        line = "Hello World !"
        r = misc.add_leading_backslashes(line)
        expected = line
        self.assertEqual(expected, r)

    def test_candidate_line(self):
        leading_backslash = "\\"
        line = "[Hello World !"
        r = misc.add_leading_backslashes(line)
        expected = leading_backslash + line
        self.assertEqual(expected, r)

    def test_candidate_line_with_leading_backslash(self):
        leading_backslash = "\\"
        line = leading_backslash + "[Hello World !"
        r = misc.add_leading_backslashes(line)
        expected = leading_backslash + line
        self.assertEqual(expected, r)


class TestGetHeadersFunc(unittest.TestCase):

    def test(self):
        section = Section("")
        section1 = Section("header1")
        section2 = Section("header2")
        sections = (section, section1, section2)
        r = misc.get_headers(sections)
        expected = {"", "header1", "header2"}
        self.assertEqual(expected, r)


class TestDecodeUnicodeFunc(unittest.TestCase):

    def test_string_1(self):
        s = r"hello \n \\n world \u02eb"
        r = misc.decode_unicode(s)
        expected = "hello \n \\n world \u02eb"
        self.assertEqual(expected, r)

    def test_string_2(self):
        s = r"hello \n world \u02eb ˫"
        r = misc.decode_unicode(s)
        expected = "hello \n world \u02eb ˫"
        self.assertEqual(expected, r)

    def test_string_3(self):
        s = r"hélicoptère"
        r = misc.decode_unicode(s)
        expected = "hélicoptère"
        self.assertEqual(expected, r)

    def test_string_4(self):
        s = r"flag for Japan \U0001f1ef\U0001f1f5"
        r = misc.decode_unicode(s)
        expected = "flag for Japan 🇯🇵"
        self.assertEqual(expected, r)

    def test_string_5(self):
        s = r"flag for Japan \U0001f1ef\U0001f1f5"
        r = misc.decode_unicode(s)
        expected = "flag for Japan \U0001f1ef\U0001f1f5"
        self.assertEqual(expected, r)


class TestEncodeUnicodeFunc(unittest.TestCase):

    def test_string_1(self):
        s = "hello \n \\n world \u02eb"
        r = misc.encode_unicode(s)
        expected = "hello \n \\n world \\u02eb"
        self.assertEqual(expected, r)

    def test_string_2(self):
        s = "hello \n\u000a world \u02eb ˫"
        r = misc.encode_unicode(s)
        expected = "hello \n\n world \\u02eb \\u02eb"
        self.assertEqual(expected, r)

    def test_string_3(self):
        s = "hélicoptère"
        r = misc.encode_unicode(s)
        expected = "hélicoptère"
        self.assertEqual(expected, r)

    def test_string_4(self):
        s = "flag for Japan \U0001f1ef\U0001f1f5"
        r = misc.encode_unicode(s)
        expected = "flag for Japan \\U0001f1ef\\U0001f1f5"
        self.assertEqual(expected, r)

    def test_string_5(self):
        s = "flag for Japan 🇯🇵"
        r = misc.encode_unicode(s)
        expected = "flag for Japan \\U0001f1ef\\U0001f1f5"
        self.assertEqual(expected, r)


class TestTidyUpNumberFuncs(unittest.TestCase):

    def test_tidy_up_integer(self):
        x = -5000000
        r = misc.tidy_up_int(x)
        expected = "-5_000_000"
        self.assertEqual(expected, r)

    def test_tidy_up_float(self):
        x = "-3780678.146538980757E-5"
        r = misc.tidy_up_float(x)
        expected = "-3_780_678.146_538_980_757E-5"
        self.assertEqual(expected, r)

    def test_tidy_up_hex(self):
        x = "-0x5A0546E8F"
        r = misc.tidy_up_hex(x)
        expected = "-0x5_A054_6E8F"
        self.assertEqual(expected, r)

    def test_tidy_up_bin(self):
        x = "-0b10110011101"
        r = misc.tidy_up_bin(x)
        expected = "-0b101_1001_1101"
        self.assertEqual(expected, r)

    def test_tidy_up_oct(self):
        x = "-0o2345623366"
        r = misc.tidy_up_oct(x)
        expected = "-0o23_4562_3366"
        self.assertEqual(expected, r)


class TestParseFloatFunc(unittest.TestCase):

    def test(self):
        x = "-3.14653898075720390738E-5"
        info = misc.parse_float(x)
        expected_left_mantissa = "-3"
        expected_right_mantissa = "14653898075720390738"
        expected_exponent = "-5"
        self.assertEqual(expected_left_mantissa, info.left_mantissa)
        self.assertEqual(expected_right_mantissa, info.right_mantissa)
        self.assertEqual(expected_exponent, info.exponent)



if __name__ == "__main__":
    unittest.main()
