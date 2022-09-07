import pathlib
from jesth import error


def render(structure):
    """
    Convert a Jesth structure into plain text

    [parameters]
    - structure: dict, Jesth structure. Each key represents a section title.
    The value of a key is the body of the section.
    The body is either a string (with newlines or none), or a list of strings

    [exceptions]
    - jesth.error.StructureError: raised if the structure isn't valid

    [return]
    Return the rendered plain text
    """
    try:
        data = _render(structure)
    except Exception as e:
        raise error.StructureError from None
    return data


def write(structure, destination):
    """
    Convert a Jesth structure into plain text then save it in a file

    [parameters]
    - structure: dict, Jesth structure. Each key represents a section title.
    The value of a key is the body of the section.
    The body is either a string (with newlines or none), or a list of strings
    - destination: str, the path (or a pathlib.Path instance) to a file in which
     the rendered Jesth text can be saved.

    [exceptions]
    - jesth.error.StructureError: raised if the structure isn't valid

    [return]
    Return the rendered plain text
    """
    data = render(structure)
    if isinstance(destination, pathlib.Path):
        destination = destination.resolve()
    with open(destination, "w") as file:
        file.write(data)
    return data


def _render(structure):
    text = []
    for header, body in structure.items():
        if header:
            header = "[{}]".format(header)
            text.append(header)
        if isinstance(body, str):
            body = body.split("\n")
        for i, line in enumerate(body):
            if line.startswith("["):
                body[i] = "\\" + line
        if not isinstance(body, str):
            body = "\n".join(body)
        text.append(body)
        if body and text[-1][-1] != "\n":
            text.append("")
    return "\n".join(text)
