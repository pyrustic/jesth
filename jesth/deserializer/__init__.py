import struct
from jesth.tagbyte import TagByte
from jesth import errors


def deserialize(raw):
    deserializer = Deserializer(raw)
    return deserializer.run()


class Deserializer:
    def __init__(self, raw):
        self._raw = raw
        self._buffer = bytearray()
        self._data = None
        self._index = 0
        self._length = len(raw)
        self._setup()

    def run(self):
        containers = list()
        self._run(containers)
        return containers[0]

    def _setup(self):
        self._check_version()
        self._index = 1

    def _run(self, containers):
        length = len(self._raw)
        while self._index < length:
            tag = read_tag(self._raw, self._index)
            self._increment()
            size = 0
            if tag == TagByte.LIST_HEAD.value:
                new_container = list()
                if len(containers) != 0:
                    containers[-1].append(new_container)
                containers.append(new_container)
            elif tag == TagByte.LIST_TAIL.value:
                if len(containers) > 1:
                    del containers[-1]
            else:
                data, size = self._interpret_tag(tag)
                if containers:
                    containers[-1].append(data)
            self._increment(size)

    def _increment(self, n=1):
        self._index += n

    def _interpret_tag(self, tag):
        if tag == TagByte.INTEGER.value:
            data, size = read_integer(self._raw, self._index)
        elif tag == TagByte.LIST_HEAD.value:
            pass
        else:
            msg = "Unknown tag byte '{}'".format(tag)
            raise errors.Error(msg)
        return data, size

    def _check_version(self):
        version = extract_version(self._raw)
        if version == 1:
            pass
        else:
            msg = "This library can't deserialize this version of Jesth Binary Format"
            raise errors.Error(msg)


def read_tag(raw, index):
    spec = "<c"
    return struct.unpack_from(spec, raw, index)[0]


def read_integer(raw, index):
    spec = "<H"
    data = struct.unpack_from(spec, raw, index)[0]
    #data = int.from_bytes(data, "little")
    return data, struct.calcsize(spec)



def extract_version(raw):
    # extract version
    spec = "<B"
    r = struct.unpack_from(spec, raw, offset=0)
    return r[0]