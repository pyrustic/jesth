import unittest
from jesth import box


class TestBoxesClasses(unittest.TestCase):

    def test_raw_string(self):
        r = box.RawString("hello world")
        self.assertIsInstance(r, str)

    def test_text(self):
        r = box.Text("hello world")
        self.assertIsInstance(r, str)

    def test_raw_text(self):
        r = box.RawText("hello world")
        self.assertIsInstance(r, str)

    def test_hex_int(self):
        r = box.HexInt(420)
        self.assertIsInstance(r, int)

    def test_oct_int(self):
        r = box.OctInt(42)
        self.assertIsInstance(r, int)

    def test_bin_int(self):
        r = box.BinInt(4)
        self.assertIsInstance(r, int)

    def test_comment_id(self):
        r1 = box.CommentID()
        r2 = box.CommentID()
        self.assertIsInstance(r1, int)
        self.assertIsInstance(r2, int)
        self.assertNotEqual(r1, r2)

    def test_comment(self):
        r = box.Comment("# this is a comment")
        self.assertIsInstance(r, str)

    def test_whitespace_id(self):
        r1 = box.WhitespaceID()
        r2 = box.WhitespaceID()
        self.assertIsInstance(r1, int)
        self.assertIsInstance(r2, int)
        self.assertNotEqual(r1, r2)

    def test_whitespace(self):
        r = box.Whitespace()
        self.assertIsInstance(r, str)


if __name__ == '__main__':
    unittest.main()
