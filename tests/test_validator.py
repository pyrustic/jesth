import unittest
import datetime
from decimal import Decimal
from jesth import validator, box
from jesth.errors import Error
from jesth.converter import ValueConverter


class TestDataValidation(unittest.TestCase):

    def test_string(self):
        data = "hello world"
        schema = "str"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = box.RawString("hello world")
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = box.Text("hello world")
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = box.RawText("hello world")
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = ''
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_int(self):
        data = 1234567
        schema = "int"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = box.HexInt(1234567)
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_float(self):
        data = 1.234567
        schema = "float"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = Decimal("1.234567")
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_bin(self):
        data = b"hello world"
        schema = "bin"
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_bool(self):
        data = True
        schema = "bool"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = False
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_complex(self):
        data = 1+2j
        schema = "complex"
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_date(self):
        data = datetime.date.today()
        schema = "date"
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_time(self):
        data = datetime.time(10, 30, 58)
        schema = "time"
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_datetime(self):
        data = datetime.datetime.now()
        schema = "datetime"
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestDataValidationWithSpec(unittest.TestCase):

    def test_string(self):
        data = "hello world"
        schema = validator.Spec("str")
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = box.RawString("hello")
        schema = validator.Spec("str", lambda x: len(x) == 5)
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        data = ''
        schema = validator.Spec("str", lambda x: len(x) == 0)
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_int(self):
        data = 42
        schema = validator.Spec("int")
        r = validator.validate(data, schema)
        self.assertTrue(r)
        #
        schema = validator.Spec("int", lambda x: x > 40 and x < 45)
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestDataInvalidation(unittest.TestCase):

    def test_string(self):
        data = "hello world"
        schema = "int"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_int(self):
        data = 1234567
        schema = "str"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_float(self):
        data = 1.234567
        schema = "int"
        r = validator.validate(data, schema)
        self.assertFalse(r)
        #
        data = Decimal("1.234567")
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_bin(self):
        data = b"hello world"
        schema = "str"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_bool(self):
        data = True
        schema = "int"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_complex(self):
        data = 1+2j
        schema = "int"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_date(self):
        data = datetime.date.today()
        schema = "datetime"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_time(self):
        data = datetime.time(10, 30, 58)
        schema = "datetime"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_datetime(self):
        data = datetime.datetime.now()
        schema = "date"
        r = validator.validate(data, schema)
        self.assertFalse(r)


class TestDataInvalidationWithSpec(unittest.TestCase):

    def test_string(self):
        data = "hello world"
        schema = validator.Spec("int")
        r = validator.validate(data, schema)
        self.assertFalse(r)
        #
        data = box.RawString("hello")
        schema = validator.Spec("str", lambda x: len(x) != 5)
        r = validator.validate(data, schema)
        self.assertFalse(r)
        #
        data = ''
        schema = validator.Spec("str", lambda x: len(x) != 0)
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_int(self):
        data = 42
        schema = validator.Spec("str")
        r = validator.validate(data, schema)
        self.assertFalse(r)
        #
        schema = validator.Spec("int", lambda x: x < 40)
        r = validator.validate(data, schema)
        self.assertFalse(r)


class TestDictValidation(unittest.TestCase):

    def test_non_empty_dict(self):
        data = {"name": "alex", "age": 420}
        # test 1
        schema = "dict"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # test 2
        schema = {"name": "str", "age": "int"}
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # test 3
        data = {"name": "alex"}
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_nested_non_empty_dict(self):
        data = {"name": "alex", "age": 420,
                "books": {"sci-fi":
                              ["book1", "book2"],
                          "thriller":
                              ["book3", "book4"]}}
        # test 1
        schema = {"name": "str", "age": "int",
                  "books": {"sci-fi":
                                ["str"],
                            "thriller":
                                ["str"]}}
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestDictInvalidation(unittest.TestCase):

    def test_type_mismatch(self):
        data = dict()
        schema = "list"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_non_empty_dict(self):
        data = {"name": "alex", "age": 420}
        # test 1
        schema = {"name": "int", "age": "int"}
        r = validator.validate(data, schema)
        self.assertFalse(r)
        # test 2
        schema = "list"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_nested_non_empty_dict(self):
        data = {"name": "alex", "age": 420,
                "books": {"sci-fi": "book1",
                          "thriller": "book2"}}
        # test 1
        schema = {"name": "str", "age": "int",
                  "books": {"sci-fi": "str",
                            "thriller": "int"}}
        r = validator.validate(data, schema)
        self.assertFalse(r)


class TestEmptyDict(unittest.TestCase):

    def test_empty_data(self):
        data = dict()
        schema = "dict"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # ---
        schema = dict()
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # ---
        schema = {"name": "str", "age": "int"}
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_empty_schema(self):
        # ---
        data = {"name": "alex"}
        schema = dict()
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestListValidation(unittest.TestCase):

    def test_list_of_int(self):
        data = [2, 3, 5, 7, 11]
        # test 1
        schema = ["int"]
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # test 2
        schema = "list"
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_list_of_int_and_str(self):
        # test 1
        data = [1, "a", 2, "b", None]
        schema = ["int", "str"]
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_nested_list_of_int(self):
        # test 1
        data = [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
        schema = ["int", ["int", ["int"]]]
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # test 2
        data = [1, 2, 3]
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_nested_list_of_int_and_str(self):
        # test 1
        data = [1, 2, 3, ["a", "b", "c", [4, 5, 6]]]
        schema = ["int", ["str", ["int"]]]
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestListInvalidation(unittest.TestCase):

    def test_type_mismatch(self):
        data = list()
        schema = "dict"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_list_of_int(self):
        data = [2, 3, 5, 7, 11]
        schema = ["str"]
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_list_of_int_and_str(self):
        data = [1, "a", 2, "b", None]
        # test 1
        schema = ["str"]
        r = validator.validate(data, schema)
        self.assertFalse(r)
        # test 2
        schema = ["int"]
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_nested_list_of_int(self):
        data = [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
        # test 1
        schema = ["int"]
        r = validator.validate(data, schema)
        self.assertFalse(r)
        # test 2
        schema = ["int", ["int"]]
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_nested_list_of_int_and_str(self):
        data = [1, 2, 3, ["a", "b", "c", [4, 5, 6]]]
        # test 1
        schema = ["int", ["str"]]
        r = validator.validate(data, schema)
        self.assertFalse(r)
        # test 2
        schema = ["int", "str", "int"]
        r = validator.validate(data, schema)
        self.assertFalse(r)


class TestEmptyList(unittest.TestCase):

    def test_empty_data(self):
        data = list()
        schema = "list"
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # ---
        schema = list()
        r = validator.validate(data, schema)
        self.assertTrue(r)
        # ---
        schema = ["int"]
        r = validator.validate(data, schema)
        self.assertTrue(r)

    def test_empty_schema(self):
        data = ["alex", "rustic"]
        schema = list()
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestComplexStructure(unittest.TestCase):

    def test(self):
        data = {"name": "alex", "age": 420,
                "books": {"sci-fi":
                              ["book1", "book2"],
                          "thriller":
                              ["book3", "book4"]},
                "misc": [1, 3.14, "pi"],
                "empty": None,
                "n": 42}
        # test 1
        schema = {"name": "str", "age": "int",
                  "books": {"sci-fi":
                                ["str"],
                            "thriller":
                                ["str"]},
                  "misc": ["int", "float", "str"],
                  "empty": "str",
                  "n": validator.Spec("int", lambda x: x > 40 and x < 45)}
        r = validator.validate(data, schema)
        self.assertTrue(r)


class TestInvalidSchema(unittest.TestCase):

    def test_invalidation(self):
        data = "hello world"
        schema = ["string"]
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_exception_raise(self):
        data = ["hello world"]
        schema = ["string"]
        with self.assertRaises(Error):
            validator.validate(data, schema)


class TestIrregularData(unittest.TestCase):

    def test_invalidation(self):
        data = ExoticData()
        schema = "str"
        r = validator.validate(data, schema)
        self.assertFalse(r)


class TestValueConverter(unittest.TestCase):

    def test_invalidation(self):
        data = CustomInteger()
        schema = "int"
        r = validator.validate(data, schema)
        self.assertFalse(r)

    def test_validation(self):
        data = CustomInteger()
        schema = "int"
        vc = ValueConverter()
        vc.integer_types.append(CustomInteger)
        r = validator.validate(data, schema, value_converter=vc)
        self.assertTrue(r)


class ExoticData:
    pass


class CustomInteger(int):
    pass


if __name__ == '__main__':
    unittest.main()
