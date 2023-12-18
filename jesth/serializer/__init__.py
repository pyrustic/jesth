import math
import struct
from jesth.converter import ValueConverter
from jesth.tagbyte import TagByte
from jesth import errors


VERSION = 1

"""
OPEN_LIST:      \x01            
CLOSE_LIST:     \x02           
INTEGER:        \x03 size data  
STRING:         \x04 size data


"""


def serialize(data):
    serializer = Serializer(data)
    return serializer.run()


class Serializer:
    def __init__(self, data, value_converter=None):
        self._data = data
        self._value_converter = value_converter if value_converter else ValueConverter()
        self._buffer = bytearray()
        self._setup()

    def run(self):
        # insert version here
        self._run(self._data)
        return bytes(self._buffer)

    def _setup(self):
        insert_version(self._buffer, VERSION)

    def _run(self, data):
        data_type = type(data)
        # integer
        if data_type in self._value_converter.integer_types:
            self._encode_integer(data)
        # list
        elif data_type in self._value_converter.list_types:
            self._encode_list(data)
        else:
            msg = "Unknown datatype {}".format(data_type)
            raise errors.Error(msg)

    def _encode_integer(self, data):
        cache = encode_integer(data)
        self._buffer.extend(cache)

    def _encode_list(self, data):
        # encode list head
        cache = encode_list_head()
        self._buffer.extend(cache)
        # iterate list
        for item in data:
            self._run(item)
        # encode list tail
        cache = encode_list_tail()
        self._buffer.extend(cache)



def encode_integer(data):
    tag = TagByte.INTEGER.value
    spec = "<cH"
    return struct.pack(spec, tag, data)


def encode_list_head():
    tag = TagByte.LIST_HEAD.value
    spec = "<c"
    return struct.pack(spec, tag)


def encode_list_tail():
    tag = TagByte.LIST_TAIL.value
    spec = "<c"
    return struct.pack(spec, tag)


def insert_version(buffer, n):
    spec = "<B"
    b = struct.pack(spec, n)
    buffer.extend(b)


def write_integer(buffer):
    spec = "<"
    buffer.extend(struct.pack(spec))



def calc_integer_size(x):
    """Return the number of bytes needed for a given integer"""
    sign_bit = 0 if x >= 0 else 1
    n_bits = sign_bit + x.bit_length()
    return math.ceil(n_bits / 8.0)
