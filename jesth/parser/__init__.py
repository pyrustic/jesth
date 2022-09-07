import os.path
import pathlib
from collections import OrderedDict


def read(source, compact=False, split_body=True):
    """
    Parse a file, return a Jesth structure

    [parameters]
    - source: Source is either a path or a pathlib.Path object
    - compact: boolean to tell if whether you want empty lines to be stripped or not.
    By default, empty lines are kept.
    - split_body: boolean to tell if you want the body to be splitted as a list of string

    [return]
    Returns a Jesth structure. A Jesth structure is a dict.
    Each key represents a section title.
    The value of a key is the body of the section.
    The body is a list of string, each string represents a line of text without the newline at end.
    """
    if isinstance(source, pathlib.Path):
        source = source.resolve()
    if not os.path.isfile(source):
        return OrderedDict()
    parser = Parser(compact=compact, split_body=split_body)
    with open(source, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip("\n")
            parser.feed(line)
    return parser.get_structure()


def parse(text, compact=False, split_body=True):
    """
    Parse a text, return a Jesth structure

    [parameters]
    - source: Source is either a text or a pathlib.Path object
    - compact: boolean to tell if whether you want whitespace and empty lines to be stripped or not.
    By default, empty lines and whitespaces are kept.
    - split_body: boolean to tell if you want the body to be splitted as a list of string

    [return]
    Returns a Jesth structure. A Jesth structure is a dict.
    Each key represents a section title.
    The value of a key is the body of the section.
    The body is a list of string, each string represents a line of text without the newline at end.
    """
    text = text.split("\n")
    parser = Parser(compact=compact, split_body=split_body)
    for line in text:
        parser.feed(line)
    return parser.get_structure()


class Parser:
    def __init__(self, compact=False, split_body=True):
        self._compact = compact
        self._split_body = split_body
        self._structure = OrderedDict()
        self._header = ""
        self._body = None
        self._active = True

    def feed(self, line):
        if not self._active:
            return
        if self._compact and (not line or line.isspace()):
            return
        if line.startswith("[") and line.endswith("]") and " " not in line:
            line = line.strip("[]")
            # clean up
            self._cleanup()
            self._body = None
            # update
            self._header = line
        else:
            if self._body is None:
                self._body = list()
            if line.startswith(r"\["):
                line = line.replace(r"\[", "[", 1)
            self._body.append(line)

    def get_structure(self):
        if not self._active:
            return self._structure
        self._cleanup()
        if not self._structure[""]:
            del self._structure[""]
        if not self._split_body:
            for header, body in self._structure.items():
                self._structure[header] = "\n".join(body)
        self._active = False

        return self._structure

    def _cleanup(self):
        # header
        if self._header is None:
            return
        if self._header not in self._structure:
            self._structure[self._header] = list()
        # body
        if self._body is None:
            return
        self._structure[self._header].extend(self._body)
