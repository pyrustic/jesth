from jesth.errors import Error
from jesth.converter import ValueConverter
from collections import OrderedDict


def validate(data, schema, value_converter=None):
    value_converter = value_converter if value_converter else ValueConverter()
    validator = Validator(schema, value_converter=value_converter)
    return validator.validate(data)


class Spec:
    def __init__(self, datatype, checker=None):
        self._datatype = datatype
        self._checker = checker

    @property
    def datatype(self):
        return self._datatype

    @property
    def checker(self):
        return self._checker


class Validator:
    def __init__(self, schema, value_converter=None):
        self._schema = schema
        self._value_converter = value_converter if value_converter else ValueConverter()

    @property
    def schema(self):
        return self._schema

    @property
    def value_converter(self):
        return  self._value_converter

    def validate(self, target):
        return self._validate(target, self._schema)

    def _validate(self, target, schema):
        if target is None:
            return True
        if isinstance(schema, str):
            return self._validate_datatype(target, schema)
        if isinstance(schema, Spec):
            return self._ensure_spec(target, schema)
        if isinstance(schema, list) or isinstance(schema, tuple):
            return self._validate_list(target, schema)
        if isinstance(schema, dict) or isinstance(schema, OrderedDict):
            return self._validate_dict(target, schema)
        msg = "Invalid schema"
        raise Error(msg)

    def _validate_list(self, target, schema):
        """Schema SHOULD be a list"""
        if type(target) not in self._value_converter.list_types:
            return False
        if not schema:
            return True
        for item in target:
            matched = False
            for expected_type in schema:
                if self._validate(item, expected_type):
                    matched = True
                    break
            if not matched:
                return False
        return True

    def _validate_dict(self, target, schema):
        if type(target) not in self._value_converter.dict_types:
            return False
        if not schema:
            return True
        for key, val in target.items():
            try:
                r = self._validate(val, schema[key])
            except KeyError as e:
                return False
            else:
                if not r:
                    return False
        return True

    def _validate_datatype(self, target, datatype):
        valid_types_map = {"dict": self._value_converter.dict_types,
                           "list": self._value_converter.list_types,
                           "bin": self._value_converter.bin_types,
                           "bool": self._value_converter.bool_types,
                           "complex": self._value_converter.complex_types,
                           "date": self._value_converter.date_types,
                           "datetime": self._value_converter.datetime_types,
                           "float": self._value_converter.float_types,
                           "int": self._value_converter.integer_types,
                           "str": (tuple(self._value_converter.string_types)
                                   + tuple(self._value_converter.raw_types)
                                   + tuple(self._value_converter.text_types)),
                           "time": self._value_converter.time_types}
        try:
            valid_types = valid_types_map[datatype]
        except KeyError as e:
            msg = "Unknown data type '{}'".format(datatype)
            raise Error(msg)
        for valid_type in valid_types:
            if type(target) == valid_type:
                return True
        return False

    def _ensure_spec(self, target, spec):
        if not self._validate_datatype(target, spec.datatype):
            return False
        if not spec.checker:
            return True
        try:
            return bool(spec.checker(target))
        except Exception as e:
            msg = "Error while running a checker"
            raise Error(msg)