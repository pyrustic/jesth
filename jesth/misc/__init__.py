"""Private miscellaneous functions. Only "split_key_value" is public"""
import os
import os.path
import pathlib
from tempfile import NamedTemporaryFile
from collections import namedtuple
from jesth import errors, const
try:
    import fcntl
except ImportError:
    fcntl = None


def write_to_file(data, dest):
    """
    Write to a file (TRY to do it atomically for GNU/Linux and MacOS)
    Check https://danluu.com/file-consistency/

    [parameters]
    - data: str, data to write to file
    - dest: a pathlib.Path instance, or a path string
    - binary_mode: boolean to tell if data should be written in dest with
      binary mode on (mode="wb")
    - encoding: defaults to "utf-8" and automatically set to None when
      binary mode is True
    """
    if isinstance(dest, pathlib.Path):
        dest = str(dest.resolve())
    if isinstance(dest, str):
        ensure_parent_dir(dest)
    else:
        msg = "Destination should be a path string or a pathlib.Path instance"
        raise errors.Error(msg)
    if os.path.isdir(dest):
        msg = "Destination shouldn't be a directory but a file path (which exists or not)"
        raise errors.Error(msg)
    WriteToFile.write(data, dest)


def split_key_value(line, sep="=", strip_whitespace=True):
    """
    Split a line (string) into key and value parts.
    The string must have a separator (defaults to "=").
    An example of a valid string is "name = John Doe ".
    The return will be: ("name": "John Doe")

    [parameters]
    - line: the string to split
    - sep: the separator, by default it is "="
    - strip_whitespace: boolean to tell whether you want whitespace at each
    side of the key and value to be stripped out or not.
    By default, the value is True.

    [return]
    Returns a ("key", "value") tuple if everything is Ok

    [exceptions]
    - errors.Error: if the separator, the key, or the value is missing,
    """
    cache = line.split(sep, maxsplit=1)
    if len(cache) != 2:
        msg = "Missing separator character '{}' in '{}'"
        msg = msg.format(sep, line)
        raise errors.Error(msg)
    key, value = cache
    if not key or key.isspace():
        msg = "Missing key in '{}'".format(line)
        raise errors.Error(msg)
    if not value or value.isspace():
        msg = "Missing value in '{}'".format(line)
        raise errors.Error(msg)
    if strip_whitespace:
        key, value = key.strip(), value.strip()
    return key, value


def correct_index(index, size, ignore_upper_bound=False):
    """
    Correct an index given to access an item in a list

    [parameter]
    - index: the integer representing the index of a list.
      This number may be positive or negative. A too big number is corrected down to
      the end index of the list.
      A negative number from -1 accesses the list from the end. A too small number
      is corrected up to 0.
      Example: give 5 the size of the list.
      Index -1 will be corrected to 4 and index 6 will be corrected to 4.
      Index -4 will be corrected to 0 same as index -10
    - size: an integer representing the size of the list

    [return]
    Return a corrected index integer
    """
    index = int(index)
    negative_size = -size
    end_index = size - 1
    if index >= size:
        if ignore_upper_bound:
            return index
        return end_index
    if index < negative_size:
        index = negative_size
    if index < 0:
        index = size - abs(index)
    return index


def ensure_parent_dir(path):
    """Make sure that parent dir exists (create it if isn't yet created)"""
    parent = os.path.dirname(path)
    try:
        os.makedirs(parent)
    except FileExistsError as e:
        pass

"""
def update_cached_refs(value, cached_refs):
    if value in cached_refs:
        raise errors.Error("Circular reference isn't allowed !")
    else:
        cached_refs.append(value)
"""

def count_indents(line):
    i = 0
    for char in line:
        if char == " ":
            i += 1
            continue
        break
    x = i / const.INDENT_WIDTH
    y = int(x)
    if x > y:
        raise errors.IndentError
    return y


def clean_leading_backslashes(line):
    """
    Remove one leading backslash only when the immediately-or-lately first non-backlash
    character on the line is an opening square bracket.
    """
    if not line or not line.startswith("\\"):
        return line
    if line.startswith(r"\["):
        line = line.replace(r"\[", "[", 1)
        return line
    char = None
    for i, char in enumerate(line):
        if char != "\\":
            break
    if char != "[":
        return line
    return line[1:]


def add_leading_backslashes(line):
    """
    Add one leading backslash only when the immediately-or-lately first non-backlash
    character on the line is an opening square bracket.
    """
    if not line:
        return line
    is_candidate = False
    for char in line:
        if char == "[":
            is_candidate = True
            break
        if char != "\\":
            break
    return "\\" + line if is_candidate else line


def get_headers(sections):
    "returns the set of headers from this list of sections"
    headers = set()
    for section in sections:
        headers.add(section.header)
    return headers


def decode_unicode(text):
    """Take in input some string that might have Unicode escape sequences.
    Output the same string with unicode escape sequences converted into
    the actual characters that they represent"""
    return text.encode("latin-1", "backslashreplace").decode("unicode-escape")


def encode_unicode(text, codec="latin-1"):
    """Convert a string into another where non-latin characters are
    replaced with Unicode escape sequences"""
    return text.encode(codec, "backslashreplace").decode(codec)


def tidy_up_float(s, width=3):
    """Tidy up a float number (str or float or decimal.Decimal)
    Example: 3.141234 -> 3.141_234
    """
    s = s if isinstance(s, str) else str(s)
    # make sure that s isn't "nan", "inf", "-inf", "infinity", ...
    for char in s:
        if char not in ("-01234.56789+eE"):
            return s
    info = parse_float(s)
    tidy_left_mantissa = tidy_up_int(info.left_mantissa)
    tidy_right_mantissa = ""
    if info.right_mantissa:
        cache = _tidy_up_right_mantissa(info.right_mantissa, width)
        tidy_right_mantissa = "." + cache
    tidy_exponent = "E" + info.exponent if info.exponent else ""
    result = tidy_left_mantissa + tidy_right_mantissa + tidy_exponent
    return result


def _tidy_up_right_mantissa(s, width):
    if not s:
        return ""
    cache = list()
    group = list()
    i = 0
    for char in s:
        if i == width:
            cache.append("".join(group))
            group = list()
            i = 0
        group.append(char)
        i += 1
    if group:
        cache.append("".join(group))
    return "_".join(cache)


def tidy_up_int(s, width=3):
    """Tidy up some int number (str or int)
    Example: 300141234 -> 300_141_234
    """
    s = s if isinstance(s, str) else str(s)
    tidy = list()
    is_negative = True if s[0] == "-" else False
    s = s.lstrip("+-")
    group = list()
    i = 0
    for char in reversed(s):
        if i == width:
            tidy.insert(0, "".join(group))
            group = list()
            i = 0
        group.insert(0, char)
        i += 1
    if group:
        tidy.insert(0, "".join(group))
    tidy = "_".join(tidy)
    result = "-" + tidy if is_negative else tidy
    return result


def tidy_up_hex(s, width=4):
    """Tidy up some hex int number (str or int)
    Example: 0xA3001F12A34 -> 0xA30_01F1_2A34
    """
    s = s if isinstance(s, str) else str(s)
    is_negative = True if s[0] == "-" else False
    s = s.lstrip("+-")
    s = s[2:]
    s = tidy_up_int(s, width=width)
    s = "0x" + s.upper()
    s = "-" + s if is_negative else s
    return s


def tidy_up_bin(s, width=4):
    """Tidy up some bin int number (str or int)
    Example: 0b10011101011 -> 0b100_1110_1011
    """
    s = s if isinstance(s, str) else str(s)
    is_negative = True if s[0] == "-" else False
    s = s.lstrip("+-")
    s = s[2:]
    s = tidy_up_int(s, width=width)
    s = "0b" + s
    s = "-" + s if is_negative else s
    return s


def tidy_up_oct(s, width=4):
    """Tidy up some oct int number (str or int)
    Example: 0o45631456202 -> 0o456_3145_6202
    """
    s = s if isinstance(s, str) else str(s)
    is_negative = True if s[0] == "-" else False
    s = s.lstrip("+-")
    s = s[2:]
    s = tidy_up_int(s, width=width)
    s = "0o" + s
    s = "-" + s if is_negative else s
    return s


FloatParts = namedtuple("FloatParts", ["left_mantissa", "right_mantissa", "exponent"])


def parse_float(s):
    """Parse a float number (string or decimal.Decimal or float), returns
    an instance of this namedtuple:
    FloatParts = namedtuple("FloatParts", ["left_mantissa", "right_mantissa", "exponent"])"""
    s = _prepare_float(s)
    # Split s at the exponent separator
    parts = s.split("E", 1)
    mantissa = parts[0]
    exponent = parts[1] if len(parts) == 2 else ""
    exponent = (exponent[1:] if exponent and exponent[0] == "+" 
                else exponent)
    # Split mantissa at the dot separator
    left_mantissa, right_mantissa = _parse_mantissa(mantissa)
    # Return the named tuple    
    return FloatParts(left_mantissa=left_mantissa, right_mantissa=right_mantissa, exponent=exponent)


def _prepare_float(s):
    if not isinstance(s, str):
        s = str(s)
    # Remove underscores, whitespaces, upper e
    cache = list()
    for c in s:
        if c in ("_", " "):
            continue
        if c == "e":
            c = "E"
        cache.append(c)
    return "".join(cache)


def _parse_mantissa(s):
    parts = s.split(".", 1)
    left_mantissa = parts[0]
    right_mantissa = parts[1] if len(parts) == 2 else ""
    return left_mantissa, right_mantissa


# --- write to file

class WriteToFile:
    @staticmethod
    def write(data, dest):
        # update encoding and mode
        binary_mode = True if isinstance(data, bytes) else False
        encoding = None if binary_mode else "utf-8"
        mode = "wb" if binary_mode else "w"
        # get parent dir and open file
        parent_dir = os.path.dirname(dest)
        # create temp file
        t = NamedTemporaryFile(prefix=".jesth_write_to_file_",
                               suffix=".temp", dir=parent_dir, delete=False)
        # write
        try:
            WriteToFile._write(data, t.name, mode, encoding)
            os.replace(t.name, dest)
            WriteToFile.sync_dir(parent_dir)
        except Exception as e:
            pass
        finally:
            try:
                os.unlink(t.name)
            except Exception as e:
                pass

    @staticmethod
    def _write(data, dest, mode, encoding):
        with open(dest, mode, encoding=encoding) as file:
            file.write(data)
            WriteToFile.sync_file(file)

    @staticmethod
    def sync_file(file):
        # file flush
        file.flush()
        # fsync the file
        fd = file.fileno()
        os.fsync(fd)
        WriteToFile.full_sync(fd)

    @staticmethod
    def sync_dir(path):
        # fsync parent dir also
        # https://man7.org/linux/man-pages/man2/fsync.2.html
        fd = os.open(path, os.O_RDONLY)
        try:
            os.fsync(fd)
            WriteToFile.full_sync(fd)
        except Exception as e:
            pass
        finally:
            os.close(fd)

    @staticmethod
    def full_sync(fd):
        # https://lists.apple.com/archives/darwin-dev/2005/Feb/msg00072.html
        if fcntl and hasattr(fcntl, "F_FULLFSYNC"):
            try:
                fcntl.fcntl(fd, fcntl.F_FULLFSYNC)
            except Exception as e:
                return False
            else:
                return True
        return False
