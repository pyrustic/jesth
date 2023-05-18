"""Errors classes"""


class Error(Exception):
    """Root error class for the Jesth Python library"""
    pass


class ConversionError(Error):
    """Error class for issues during data conversion"""
    pass


class IndentError(Error):
    """Indent error while parsing a section body"""
    pass
