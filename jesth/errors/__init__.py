"""Errors classes"""


class Error(Exception):
    """Root errors class for the Jesth Python library"""
    pass


class ConversionError(Error):
    """Error class for issues during data conversion"""
    pass


class IndentError(Error):
    """Indent errors while parsing a section body"""
    pass
