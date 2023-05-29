import unittest
import jesth


class TestRootImports(unittest.TestCase):

    def test_wrong_import(self):
        with self.assertRaises(AttributeError):
            jesth.abracadabra

    def test(self):
        jesth.Document
        jesth.Section
        jesth.parse
        jesth.render
        jesth.read
        jesth.write
        jesth.create_dict
        jesth.flatten_dict
        jesth.ValueConverter
        jesth.split_key_value
        jesth.Parser
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
