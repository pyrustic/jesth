import zlib
from jesth.dataformat.text import encode as jesth_encode, decode as jesth_decode


def serialize(data, value_converter=None):
    data = jesth_encode(data).encode("utf-8")
    return zlib.compress(data, 6)


def deserialize(raw, value_converter=None):
    data = zlib.decompress(raw).decode("utf-8")
    return jesth_decode(data)
