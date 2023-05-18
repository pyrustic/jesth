"""Definition of the Section class"""
from collections import OrderedDict
from jesth import converter, error
from jesth.converter import ValueConverter


class Section:
    """A section is the main unit of a jesthFile. It's composed of a header and a body"""
    def __init__(self, header, body=None, *, value_converter=None):
        """
        Init a section

        [parameters]
        - header: the header (string) of the section
        - body: the body of the section is a string, a list of strings or a dict.
        Beware, if the body is a dict, instantiating this class may raise exceptions.
        For example, if the body contains circular references, an exception will be raised.
        Use the method ".update" if you want to submit a dict as body
        - value_converter: instance of ValueConverter to customize value encoding
        """
        self._header = header
        self._body = list()
        self._value_converter = value_converter if value_converter else ValueConverter()
        # update body
        self.update(body)

    @property
    def header(self):
        return self._header

    @property
    def body(self):
        """The body in its base form, i.e., a list of strings !"""
        return self._body

    @property
    def value_converter(self):
        return self._value_converter

    def get_dict(self, default=None, fallback=None, *, strict=True):
        """
        Try to convert the body of this section into a dict.
        Return fallback if failed to convert

        [parameters]
        - default: Value to return if the body has been successfully converted into an empty dict.
        Note that `default` will be updated to contain an empty OrderedDict if you leave it set to None.
        - fallback: Value to return if the attempt to convert the body into a dict failed
        - strict: set True if you don't want to preserve comments and whitespaces

        [return]
        If everything is ok, a dict (OrderedDict) will be returned.
        Else the value of `default` or `fallback` will be returned.
        """
        default = OrderedDict() if default is None else default
        try:
            return self.make_dict(default=default, strict=strict)
        except Exception as e:
            return fallback

    def make_dict(self, default=None, *, strict=True):
        """
        Try to convert the body of this section into a dict (OrderedDict).
        Raise an exception if an error occurs !
        Return `default` if the body has been created but is empty

        [parameters]
        - default: Value to return if the body has been successfully converted into an empty dict. 
        Note that `default` will be updated to contain an empty OrderedDict if you leave it set to None.
        - strict: set True if you don't want to preserve comments and whitespaces

        [return]
        If everything is ok, a dict (OrderedDict) will be returned or the value of `default`
        Exceptions will be raised whenever a problem will arise !
        """
        default = OrderedDict() if default is None else default
        data = converter.make_dict(self._body,
                                   value_converter=self._value_converter,
                                   strict=strict)
        return data if data else default

    def update(self, body):
        """Update the entire body. The new body may be string, list of strings or a dict.
        Beware, if the body is a dict, instantiating this class may raise exceptions.
        For example, if the body contains circular references, an exception will be raised."""
        self._body = ensure_body(body,
                                 value_converter=self._value_converter)


def ensure_body(body, value_converter=None):
    """Convert the body in the canonical base form: a list of string."""
    body = body if body else list()
    # string
    if isinstance(body, str):
        lines = body.split("\n")
        return lines
    # dict
    if isinstance(body, dict):  # OrderedDict subclasses dict
        return converter.flatten_dict(body, value_converter=value_converter)
    # list
    if isinstance(body, list):
        body = [line.replace("\n", "\\n") for line in body]
        return body
    raise error.ConversionError
