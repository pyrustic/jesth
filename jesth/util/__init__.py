
def get_key_value(line, sep="=", strip_whitespace=True):
    """
    Split a string into key and value parts.
    The string must have a separator defined as an argument.
    By default, the separator is ":".
    An example of a valid string is "name: John Doe ".
    The result will be: ("name": "John Doe")

    [parameters]
    - line: the string to split
    - sep: the separator, by default it is ":"
    - strip_whitespace: boolean to tell whether you want whitespace to be stripped out or not.
    By default, the value is True.

    [return]
    Always returns a tuple. If the key doesn't exist, it will be an empty string
    """
    cache = line.split(sep, maxsplit=1)
    if len(cache) == 2:
        key, value = cache
    else:
        key, value = "", cache[0]
    if strip_whitespace:
        return key.strip(), value.strip()
    return key, value
