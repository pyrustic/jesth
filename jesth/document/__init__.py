"""Document class for creating model for Jesth data or to interacting with a Jesthfile"""
import pathlib
from jesth import misc, validator
from jesth.section import Section
from jesth.renderer import write, render
from jesth.converter import ValueConverter
from jesth.errors import Error


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
        self._schema = None
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
    def schema(self):
        return self._schema

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
        n = len(self._sections)
        self._insert(n, header, body)

    def insert(self, index, header, body=None):
        """
        Create a new section then insert it in the document at a specific index

        [parameters]
        - index: integer index (absolute index). Accepts -1 to mimic the "append" method
        - header: the header (string) of the new section
        - body: the body of this section as a string or a list of strings
        """
        n = len(self._sections)
        index = misc.correct_index(index, n,
                                   ignore_upper_bound=True) if n else 0
        self._insert(index, header, body)

    def set(self, index, header, body=None):
        """
        Set a section at a specific index of the document

        [parameters]
        - index: the index integer
        - header: the header string of the section
        - body: the body of the section, may be a list of string, a dictionary,
          or a text string
        """
        n = len(self._sections)
        index = misc.correct_index(index, n) if n else 0
        # find section at same index then remove it
        cache = self._find_section_to_remove(index)
        if cache:
            h, i = cache
            self.remove(header=h, sub_index=i)
        # insert new section
        self._insert(index, header, body)

    def get(self, header, sub_index=0):
        """
        Get X named section object located at Y index relatively to others sections with same header

        [parameters]
        - header: the header (string) of the section
        - index: integer index, relatively to the section
        family (sections sharing this same header).
        Defaults to 0, thus will be returned, the first section with this header relatively
        to this header family.

        [return]
        Returns a section or None
        """
        try:
            n = len(self._model[header])
        except KeyError:
            return None
        sub_index = misc.correct_index(sub_index, n) if n else 0
        section = None
        try:
            section = self._model[header][sub_index]
        except IndexError:
            pass
        return section

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

    def bind_schema(self):  # TODO
        pass

    def unbind_schema(self):  # TODO
        pass

    def validate(self, *headers):  # TODO
        """
        Validate this document
        [parameters]
        - *headers: headers to validate. If you ignore this parameter, the document will
        be checked against the schema.
        [return]
        Return true if the document is valid. Raise an exception if the schema is missing
        """
        if self.schema is None:
            msg = "Missing schema"
            raise Error(msg)
        if not isinstance(self.schema, dict):
            msg = "The schema must be a dictionary whose keys represent the section headers"
            raise Error(msg)
        for key, val in self.schema.items():
            validator.validate()



        #validator.validate(self.)

    def remove(self, header, sub_index=-1):
        """
        Remove a section from this document

        [parameters]
        - header: the header of the section to remove
        - index: the index (integer) of the section relatively to
        its family (sections sharing same header).
        Defaults to -1, thus the last section of the given header family will be removed
        from the document
        """
        try:
            n = len(self._model[header])
        except KeyError:
            return
        sub_index = misc.correct_index(sub_index, n)
        if n == 0:
            del self._model[header]
        else:
            try:
                del self._model[header][sub_index]
            except IndexError:
                pass
        i1 = i2 = 0
        for section in self._sections:
            if section.header == header:
                if i2 == sub_index:
                    del self._sections[i1]
                    break
                i2 += 1
            i1 += 1

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
        self._model = dict()
        for section in self._sections:
            header = section.header
            if header not in self._model:
                self._model[header] = list()
            self._model[header].append(section)

    def _insert(self, index, header, body):
        section = Section(header, body=body,
                          value_converter=self._value_converter)
        self._sections.insert(index, section)
        self._update_model(header, index, section)

    def _update_model(self, header, index, section):
        if header not in self._model:
            self._model[header] = list()
        self._model[header].insert(index, section)

    def _find_section_to_remove(self, index):
        # find section at same index (the section to remove)
        header = None
        for i, section in enumerate(self._sections):
            if i == index:
                header = section.header
        if header is None:
            return
        i1 = i2 = 0
        for section in self._sections:
            if i1 == index:
                return header, i2
            if section.header == header:
                i2 += 1
            i1 += 1
