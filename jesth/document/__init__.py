"""Document class for creating model for Jesth data or to interacting with a Jesthfile"""
import pathlib
from collections import OrderedDict
from jesth import misc
from jesth.section import Section
from jesth.renderer import write, render
from jesth.converter import ValueConverter


class Document:
    """Create a model for Jesth data or for interacting with a JesthFile"""
    def __init__(self, path=None, sections=None, *, value_converter=None):
        """
        Init the document

        [parameters]
        - path: if the document is linked to a JesthFile,`path` contains the path to this file.
            Path might also be a pathlib.Path instance.
        - sections: list of sections (or tuple)
        - value_converter: an instance of jesth.converter.ValueConverter
        """
        self._path = str(path.resolve()) if isinstance(path, pathlib.Path) else path
        sections = sections if sections else list()
        self._sections = list(sections) if not isinstance(sections, list) else sections
        self._value_converter = value_converter if value_converter else ValueConverter()
        self._is_new = False
        self._model = None
        self._setup()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, val):
        self._path = val

    @property
    def sections(self):
        return self._sections.copy()

    @sections.setter
    def sections(self, val):
        self._sections = val
        self._create_model()

    @property
    def value_converter(self):
        return self._value_converter

    @property
    def headers(self):
        if not self._sections:
            return None
        return misc.get_headers(self._sections)

    def render(self, *headers, spacing=1):
        """
        Render the entire document or a specific set of sections, i.e.,
        returns a Jesth string that may be stored in a file.

        [parameters]
        - *headers: Headers of sections to render. Omitting this will render the entire section
        - spacing: number of empty lines between two adjacent sections. Defaults to 1 empty line.

        [return]
        Returns a string that contains sections (each made of square-brackets delimited header
        and associated body)
        """
        return render(self, *headers,
                      spacing=spacing)

    def save(self):
        """
        Save the recent modifications if this document is linked to a JesthFile,
         i.e., the path parameter has been set.

        [return]
        Returns True or False
         """
        if not self._path:
            return False
        write(self, destination=self._path)
        return True

    def save_to(self, path):
        """
        Save the document in a specific filename

        [parameters]
        - path: path to filename. Path may be a pathlib.Path instance
        """
        if isinstance(path, pathlib.Path):
            path = str(path.resolve())
        write(self, destination=path)

    def append(self, header, body=None):
        """
        Create a new section then append it to the end of this document

        [parameters]
        - header: the header (string) of the new section
        - body: the body of this section as a string or a list of strings
        """
        self._insert(len(self._sections), header, body)

    def insert(self, index, header, body=None):
        """
        Create a new section then insert it in the document at a specific index

        [parameters]
        - index: integer index (absolute index). Accepts -1 to mimic the "append" method
        - header: the header (string) of the new section
        - body: the body of this section as a string or a list of strings
        """
        index = len(self._sections) if index == -1 else index
        self._insert(index, header, body)

    def get(self, header, index=-1):
        """
        Get X named section object located at Y index relatively to others sections with same header

        [parameters]
        - header: the header (string) of the section
        - index: integer index, relatively to the section
        family (sections sharing this same header).
        Defaults to -1, thus will be returned, the last section with this header relatively
        to this header family.

        [return]
        Returns a section or None
        """
        if header not in self._model:
            return None
        return self._model[header][index]

    def get_all(self, header):
        """
        Get all sections sharing same header

        [parameters]
        - header: the header (string) of the sections

        [return]
        Returns a list of sections whose headers match with the `header` parameter.
        """
        return self._model.get(header, list()).copy()

    def count(self, header):
        """
        Count the number of sections whose headers match with the
        `header` parameter

        [parameters]
        - header: the header (string) of the sections

        [return]
        Returns the integer number of sections matching with the `header` parameter
        """
        if header not in self._model:
            return 0
        return len(self._model[header])

    def remove(self, header, index=-1):
        """
        Remove a section from this document

        [parameters]
        - header: the header of the section to remove
        - index: the index (integer) of the section relatively to
        its family (sections sharing same header).
        Defaults to -1, thus the last section of the given header family will be removed
        from the document
        """
        if header not in self._model:
            return
        if self._model[header]:
            del self._model[header][index]
        else:
            del self._model[header]
        index = len(self._sections) if index == -1 else index
        i = len(self._sections) - 1
        for _ in reversed(self._sections):
            if i == index:
                del self._sections[i]
                break

    def remove_all(self, header):
        """
        Remove all sections with this specific header

        [parameters]
        - header: the header of the section to remove
        """
        if header not in self._model:
            return
        del self._model[header]
        i = len(self._sections) - 1
        for section in reversed(self._sections):
            if section.header == header:
                del self._sections[i]
            i -= 1

    def _setup(self):
        self._create_model()

    def _create_model(self):
        self._model = OrderedDict()
        for section in self._sections:
            header = section.header
            if header not in self._model:
                self._model[header] = list()
            self._model[header].append(section)

    def _insert(self, index, header, body):
        section = Section(header, body=body,
                          value_converter=self._value_converter)
        if index == 0 or index == len(self._sections):
            self._sections.insert(index, section)
            self._update_model(header, index, section)
        else:
            self._sections.insert(index, section)
            self._create_model()

    def _update_model(self, header, index, section):
        if header not in self._model:
            self._model[header] = list()
        self._model[header].insert(index, section)
