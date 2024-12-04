"""This module exposes render and write functions"""
import pathlib
from jesth import misc


def render(document, *headers, spacing=1):
    """
    Convert a jesth document into plain text

    [parameters]
    - document: an instance of jesth.document.Document
    - *headers: Headers of sections to render. Omitting this will render the entire section
    - spacing: number of empty lines between two adjacent sections. Defaults to 1 empty line.

    [return]
    Returns a string that contains sections (each made of square-brackets
    delimited header and associated body). This string can be stored in a file,
    thus creating a JesthFile
    """
    cache = list()
    for i, section in enumerate(document.sections):
        if headers and section.header not in headers:
            continue
        safe_body = [misc.add_leading_backslashes(line)
                     for line in section.body]
        body = "\n".join(safe_body)
        header = ("" if i == 0 and section.header == ""
                  else "[{}]".format(section.header))
        if body:
            header = header + "\n" if header else header
            text = "{header}{body}".format(header=header, body=body)
        else:
            text = "{header}".format(header=header)
        cache.append(text)
    spacing = ("\n" * spacing) + "\n"
    return spacing.join(cache)


def write(document, destination):
    """
    Convert a jesth document into plain text then write it in a file

    [parameters]
    - document: an instance of jesth.document.Document
    - destination: path string, or pathlib.Path instance to a file in which
     the rendered Jesth text can be saved.

    [return]
    Returns the rendered plain text
    """
    data = render(document)
    if isinstance(destination, pathlib.Path) or isinstance(destination, str):
        misc.write_to_file(data, destination)
    else:
        destination.write(data.encode("utf-8"))
    return data
