"""This module exposes read and parse functions that return a document instance"""
import pathlib
from jesth import misc
from jesth.converter import ValueConverter
from jesth.document import Document
from jesth.section import Section


def read(source, value_converter=None):
    """
    Read a file, returns a document (jesth.document.Document)

    [parameters]
    - source: source is either a path string or a pathlib.Path object,
     or a binary file-like object
    - value_converter: instance of jesth.converter.ValueConverter to customize value encoding

    [return]
    Returns an instance of jesth.document.Document
    """
    value_converter = value_converter if value_converter else ValueConverter()
    if isinstance(source, pathlib.Path):
        source = str(source.resolve())
    parser = Parser(value_converter=value_converter)
    if isinstance(source, str):
        with open(source, "rb") as file:
            _read_file_object(file, parser)
    else:
        _read_file_object(source, parser)
    document = Document(source, sections=parser.sections,
                        value_converter=value_converter)
    return document


def parse(text, value_converter=None):
    """
    Parse a text, return a document

    [parameters]
    - text: text string
    - value_converter: instance of jesth.converter.ValueConverter to customize value encoding

    [return]
    Returns an instance of jesth.document.Document
    """
    value_converter = value_converter if value_converter else ValueConverter()
    text = text.split("\n")
    parser = Parser(value_converter=value_converter)
    for line in text:
        if not parser.feed(line):
            break
    document = Document(sections=parser.sections,
                        value_converter=value_converter)
    return document


def _read_file_object(file, parser):
    while True:
        line = file.readline()
        if not line:
            break
        line = line.decode("utf-8").rstrip("\n")
        if not parser.feed(line):
            break


class Parser:
    def __init__(self, value_converter=None):
        self._value_converter = value_converter if value_converter else ValueConverter()
        self._sections = list()
        self._header = None
        self._body = None
        self._feedable = True

    @property
    def value_converter(self):
        return self._value_converter

    @property
    def feedable(self):
        """Isn't anymore feedable when the `[[END]]` tag is encountered"""
        return self._feedable

    @property
    def sections(self):
        self._update()
        return self._sections

    def feed(self, line):
        #if not line or line.isspace():
        #    return
        if not self._feedable:
            return False
        if line.rstrip().lower() == "[[end]]":
            self._update()
            self._feedable = False
            return False
        if line.startswith("["):
            cache = line.rstrip()
            if cache.endswith("]"):
                self._update()
                self._header = cache.strip("[]")
                return True
        line = misc.clean_leading_backslashes(line)
        if self._body is None:
            self._body = list()
        self._body.append(line)
        return True

    def _update(self):
        if not self._feedable:
            return
        if self._header is None and self._body is None:
            return
        if self._header is None and self._body is not None:
            header, body = "", self._body
        elif self._header is not None and self._body is None:
            header, body = self._header, list()
        else:
            header, body = self._header, self._body
        self._strip_section_spacing(body)
        section = Section(header, body, value_converter=self._value_converter)
        self._sections.append(section)
        self._header = self._body = None

    def _strip_section_spacing(self, body):
        for line in reversed(body):
            if line and not line.isspace():
                return
            del body[-1]
