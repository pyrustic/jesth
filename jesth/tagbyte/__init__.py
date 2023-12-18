from enum import Enum


class TagByte(Enum):
    LIST_HEAD = b"\x01"
    LIST_TAIL = b"\x02"
    DICT_KEYS_HEAD = b"\x03"
    DICT_KEYS_TAIL = b"\x04"
    INTEGER = b"\x05"
    STRING = b"\x06"
