from jesth.parser import read
from jesth import misc
from jesth.converter import flatten_dict, create_dict


def load(source, value_converter=None):
    """
    Load data from a file or file object
    """
    doc = read(source, value_converter)
    if not doc.sections:
        return None
    section = doc.sections[0]
    if section.header != "":
        return None
    body = section.to_dict()
    if not body:
        return None
    return body.get("data")


def dump(data, destination, value_converter=None):
    body = encode(data, value_converter)
    misc.write_to_file(body, destination)


def encode(data, value_converter=None):
    body = {"data": data}
    body = flatten_dict(body, value_converter=value_converter)
    return "\n".join(body)


def decode(text, value_converter=None):
    data = create_dict(text, value_converter=value_converter)
    return data.get("data")
