"""Boxes to hold contents like Jesth Comments, raw texts, or whitespaces..."""
import threading


class RawString(str):
    """Box to hold raw string, i.e., string between two single quotes"""
    pass


class Text(str):
    """Box to hold Text, i.e., multiline string with unicode escape sequences support"""
    pass


class RawText(str):
    """Box to hold raw Text, i.e., multiline string without unicode escape sequences support"""
    pass


class HexInt(int):
    """Box to hold hexadecimal integer"""
    pass


class OctInt(int):
    """Box to hold octal integer"""
    pass


class BinInt(int):
    """Box to hold binary integer"""
    pass


class CommentID(int):
    """Box to hold an unique comment id"""
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, N.generate_id())


class Comment(str):
    """Box to hold a Jesth comment"""
    pass


class WhitespaceID(int):
    """Box to hold an unique whitespace id"""
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, N.generate_id())


class Whitespace(str):
    """Box to hold a whitespace"""
    pass


class N:
    """Private class to generate unique identifiers (thread-safe)"""
    _lock = threading.Lock()
    _count = 0

    @classmethod
    def generate_id(cls):
        """Generate an unique integer identifier (thread-safe)"""
        with cls._lock:
            cls._count += 1
            return cls._count
