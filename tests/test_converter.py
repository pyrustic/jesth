import decimal
import unittest
import datetime
from decimal import Decimal
from jesth import box, errors
from jesth.converter import ValueConverter, create_dict, flatten_dict


BODY = r"""
# strings
string = "Hello "World" ! \\ \n \\n \\u000A ˫"
raw_string = 'Hello 'World' ! \n \\n \u000A ˫'
empty_string = ""
empty_raw_string = ''

# scalars
int = -4_200_000
hex_int = 0xAE1F
oct_int = 0o3427
bin_int = 0b101_0011_1010_1010
float = 3.141
decimal_float = 3.141_592_653_589_793_238_46E-10
complex = -4.2+6.9i
bool_1 = true
bool_2 = false

# null value
empty_value = null

# date and time (ISO 8601)
datetime = 2020-10-20T15:35:57Z
date = 2020-10-20
time = 15:35:57

# text
text = (text)
    Stand a little less \\n
    between me and the sun. ˫
    ---
empty_text = (text)
    ---

# raw text
raw = (raw)
    The foundation of every state
    is the education of its youth. ˫
    \u000A - WYSIWYG - C:\home\alex
    ---
empty_raw = (raw)
    ---

# bin data (standard base64 - RFC 4648)
bin = (bin)
    TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwg
    c2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduY
    SBhbGlxdWEu
    ---
empty_bin = (bin)
    ---

# list collection
list = (list)
    "Item 1"
    "Item 2"
    "Item 3"
    # nested list
    (list)
        "item i"
        "item ii"
        "item iii"
empty_list = (list)

# dict collection
dict = (dict)
    key_1 = "value"
    key_2 = (list)
        "item i"
        "item ii"
        # nested dict
        (dict)
            project = "Jesth: Just Extract Sections Then Hack !"
            description = "Next level human-readable data serialization format"
            repository = 'https://github.com/pyrustic/jesth'
            author = "alex rustic"
empty_dict = (dict)
"""


class TestConversionFuncs(unittest.TestCase):

    def test(self):
        # Make a dict from BODY
        dict_body = create_dict(BODY, strict=False)
        # Flatten the dict
        flat_body = flatten_dict(dict_body)
        # Make text from flatten body then compare with BODY
        text = "\n".join(flat_body)
        self.assertEqual(BODY, text)


class TestValueConverterClass(unittest.TestCase):

    def setUp(self):
        self._value_converter = ValueConverter()

    def test_bin_encoder(self):
        val = b"Hello World"
        r = self._value_converter.encode(val)
        expected = "(bin)"
        self.assertEqual(expected, r)

    def test_bool_encoder(self):
        # test True
        val = True
        r = self._value_converter.encode(val)
        expected = "true"
        self.assertEqual(expected, r)
        # test False
        val = False
        r = self._value_converter.encode(val)
        expected = "false"
        self.assertEqual(expected, r)

    def test_complex_encoder(self):
        val = 3.14 + 5j
        r = self._value_converter.encode(val)
        expected = "3.14+5i"
        self.assertEqual(expected, r)

    def test_date_encoder(self):
        val = datetime.date(2023, 5, 1)
        r = self._value_converter.encode(val)
        expected = "2023-05-01"
        self.assertEqual(expected, r)

    def test_datetime_encoder(self):
        # Datetime 1 (datetime with T between date and time)
        val = datetime.datetime(2023, 5, 1, 8, 10, 32,
                                tzinfo=datetime.timezone.utc)
        r = self._value_converter.encode(val)
        expected = "2023-05-01T08:10:32Z"
        self.assertEqual(expected, r)
        # Datetime 3 (datetime with +8 hours offset)
        timezone = datetime.timezone(datetime.timedelta(hours=8))
        val = datetime.datetime(2023, 5, 1, 8, 10, 32,
                                tzinfo=timezone)
        r = self._value_converter.encode(val)
        expected = "2023-05-01T08:10:32+08:00"
        self.assertEqual(expected, r)

    def test_float_encoder(self):
        val = 3.14E2
        r = self._value_converter.encode(val)
        expected = "314.0"
        self.assertEqual(expected, r)

    def test_custom_float_encoder(self):
        val = Decimal("3.148739534274212841284649")
        r = self._value_converter.encode(val)
        expected = "3.148_739_534_274_212_841_284_649E0"
        self.assertEqual(expected, r)

    def test_integer_encoder(self):
        # base 10 integer
        val = -123456789
        r = self._value_converter.encode(val)
        expected = "-123_456_789"
        self.assertEqual(expected, r)
        # hex integer
        val = box.HexInt(0x13FA89D23E9)
        r = self._value_converter.encode(val)
        expected = "0x13F_A89D_23E9"
        self.assertEqual(expected, r)
        # bin integer
        val = box.BinInt(0b1001011011100)
        r = self._value_converter.encode(val)
        expected = "0b1_0010_1101_1100"
        self.assertEqual(expected, r)
        # oct integer
        val = box.OctInt(0o3727352737251)
        r = self._value_converter.encode(val)
        expected = "0o3_7273_5273_7251"
        self.assertEqual(expected, r)

    def test_null_encoder(self):
        val = None
        r = self._value_converter.encode(val)
        expected = "null"
        self.assertEqual(expected, r)

    def test_raw_encoder(self):
        val = box.RawText()
        r = self._value_converter.encode(val)
        expected = "(raw)"
        self.assertEqual(expected, r)

    def test_string_encoder(self):
        # Processed string
        val = "Hello \n \\n \n World ! \u02eb"
        r = self._value_converter.encode(val)
        expected = r'"Hello \n \\n \n World ! ˫"'
        self.assertEqual(expected, r)
        # Raw string
        val = box.RawString("Raw \n \\n \u000A \\\\n String ! ˫")
        r = self._value_converter.encode(val)
        expected = r"'Raw \n \n \n \\n String ! ˫'"
        self.assertEqual(expected, r)

    def test_text_encoder(self):
        val = box.Text()
        r = self._value_converter.encode(val)
        expected = "(text)"
        self.assertEqual(expected, r)

    def test_time_encoder(self):
        val = datetime.time(10, 30, 58)
        r = self._value_converter.encode(val)
        expected = "10:30:58"
        self.assertEqual(expected, r)

    def test_fallback_encoder(self):
        val = CustomClass()
        r = self._value_converter.encode(val)
        expected = '"My Custom Class"'
        self.assertEqual(expected, r)

    def test_bin_decoder(self):
        val = "(bin)"
        r = self._value_converter.decode(val)
        expected = list()
        self.assertEqual(expected, r)

    def test_bool_decoder(self):
        # test True
        val = "true"
        r = self._value_converter.decode(val)
        expected = True
        self.assertEqual(expected, r)
        # test False
        val = "false"
        r = self._value_converter.decode(val)
        expected = False
        self.assertEqual(expected, r)

    def test_complex_decoder(self):
        val = "3.14+5i"
        r = self._value_converter.decode(val)
        expected = 3.14+5j
        self.assertEqual(expected, r)

    def test_date_decoder(self):
        val = "2023-05-01"
        r = self._value_converter.decode(val)
        expected = datetime.date(2023, 5, 1)
        self.assertEqual(expected, r)

    def test_datetime_decoder(self):
        # Datetime 1 (datetime with T between date and time)
        val = "2023-05-01T08:10:32Z"
        r = self._value_converter.decode(val)
        expected = datetime.datetime(2023, 5, 1, 8, 10, 32,
                                     tzinfo=datetime.timezone.utc)
        self.assertEqual(expected, r)
        # Datetime 2 (datetime with space between date and time)
        val = "2023-05-01 08:10:32Z"
        r = self._value_converter.decode(val)
        self.assertEqual(expected, r)
        # Datetime 3 (datetime with +8 hours offset)
        val = "2023-05-01 08:10:32+08:00"
        r = self._value_converter.decode(val)
        timezone = datetime.timezone(datetime.timedelta(hours=8))
        expected = datetime.datetime(2023, 5, 1, 8, 10, 32,
                                     tzinfo=timezone)
        self.assertEqual(expected, r)

    def test_float_decoder(self):
        # float 1
        val = "3.14E9"
        r = self._value_converter.decode(val)
        expected_type = decimal.Decimal
        expected_r = decimal.Decimal("3.14E9")
        self.assertIs(expected_type, type(r))
        self.assertEqual(expected_r, r)
        # float 2
        val = "3.1437"
        r = self._value_converter.decode(val)
        expected_type = float
        expected_r = 3.1437
        self.assertIs(expected_type, type(r))
        self.assertEqual(expected_r, r)
        # float 3
        val = "3.1437E0"
        r = self._value_converter.decode(val)
        expected_type = decimal.Decimal
        expected_r = decimal.Decimal("3.1437E0")
        self.assertIs(expected_type, type(r))
        self.assertEqual(expected_r, r)

    def test_custom_float_decoder(self):
        self._value_converter.float_decoder = Decimal
        val = "3.148739534274212841284649"
        r = self._value_converter.decode(val)
        expected = Decimal("3.148739534274212841284649")
        self.assertEqual(expected, r)

    def test_integer_decoder(self):
        # base 10 integer
        val = "-123_456_789"
        r = self._value_converter.decode(val)
        expected = -123456789
        self.assertEqual(expected, r)
        self.assertTrue(isinstance(r, int))
        # hex integer
        val = "0x13F_A89D_23E9"
        r = self._value_converter.decode(val)
        expected = 0x13F_A89D_23E9
        self.assertEqual(expected, r)
        self.assertTrue(isinstance(r, box.HexInt))
        # bin integer
        val = "0b1_0010_1101_1100"
        r = self._value_converter.decode(val)
        expected = 0b1_0010_1101_1100
        self.assertEqual(expected, r)
        self.assertTrue(isinstance(r, box.BinInt))
        # oct integer
        val = "0o3_7273_5273_7251"
        r = self._value_converter.decode(val)
        expected = 0o3_7273_5273_7251
        self.assertEqual(expected, r)
        self.assertTrue(isinstance(r, box.OctInt))

    def test_null_decoder(self):
        val = "null"
        r = self._value_converter.decode(val)
        expected = None
        self.assertEqual(expected, r)

    def test_raw_decoder(self):
        val = "(raw)"
        r = self._value_converter.decode(val)
        expected = list()
        self.assertEqual(expected, r)

    def test_string_decoder(self):
        # Processed string
        val = r'"Hello \n \\n \u000A World ! ˫"'
        r = self._value_converter.decode(val)
        expected = "Hello \n \\n \n World ! \u02eb"
        self.assertEqual(expected, r)
        # Raw string
        val = r"'Hello \n \\n \u000A World ! ˫'"
        r = self._value_converter.decode(val)
        expected = "Hello \\n \\\\n \\u000A World ! ˫"
        self.assertEqual(expected, r)

    def test_text_decoder(self):
        val = "(text)"
        r = self._value_converter.decode(val)
        expected = list()
        self.assertEqual(expected, r)

    def test_time_decoder(self):
        val = "10:30:58"
        r = self._value_converter.decode(val)
        expected = datetime.time(10, 30, 58)
        self.assertEqual(expected, r)

    def test_fallback_decoder(self):
        val = "goto"
        with self.assertRaises(errors.ConversionError):
            self._value_converter.decode(val)


class CustomClass:
    def __str__(self):
        return "My Custom Class"


if __name__ == '__main__':
    unittest.main()
