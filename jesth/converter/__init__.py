"""Classes and functions to convert a section body into a Python dict, or flatten a Python dict into a section body"""
import datetime
import base64
from decimal import Decimal
from collections import OrderedDict, namedtuple
from jesth import errors, misc, const
from jesth.box import HexInt, OctInt, BinInt, RawString,\
    Text, RawText, CommentID, Comment, WhitespaceID, Whitespace


def create_dict(body, value_converter=None, strict=True):
    """
    Convert a section body into a Python dict

    [parameters]
    - body: string or list of strings
    - value_converter: instance of ValueConverter to customize value encoding
    - strict: when strict is True, comments and whitespaces aren't preserved

    [return]
    Returns a Python dict (type customizable with ValueConverter)

    [exceptions]
    - jesth.errors.ConversionError: raised when an errors occured while doing conversion
    """
    value_converter = value_converter if value_converter else ValueConverter()
    # base form (as a regular string)
    if isinstance(body, str):
        body = body.split("\n")
    return BaseToDict.run(body, value_converter, strict)


def flatten_dict(data, value_converter=None):
    """
    Convert a Python dict into a list of strings (section body in the base form)

    [parameters]
    - data: Python dict
    - value_converter: instance of ValueConverter to customize value encoding

    [return]
    Returns a list of strings
    """
    value_converter = value_converter if value_converter else ValueConverter()
    return DictToBase.run(data, value_converter)


class BaseToDict:
    @staticmethod
    def run(lines, value_converter=None, strict=True):
        value_converter = value_converter if value_converter else ValueConverter()
        stack = list()
        root_container = value_converter.dict_type()
        root_context = Context("dict", root_container, 0)
        stack.append(root_context)
        for lineno, line in enumerate(lines):
            # remove line breaks
            line = line.replace("\n", "\\n")
            context = stack[-1]
            line, indents = BaseToDict._prepare_line(line, context)
            # same indent
            if indents == context.indents:
                pass
            # lower indent
            elif indents < context.indents:
                BaseToDict._cleanup_stack(stack, value_converter, indents, strict)
            # exaggerated forward indent
            else:
                msg = "Expected {} or less indents at line '{}'"
                msg = msg.format(context.indents, line)
                raise errors.IndentError(msg)
            # process line
            try:
                BaseToDict._process_line(line, stack, value_converter,
                                         strict)
            except Exception as e:
                msg = "Error on line {}: {}{}"
                str_e = str(e)
                str_e = ": " + str_e if str_e else str_e
                msg = msg.format(lineno+1, type(e).__name__, str_e)
                raise type(e)(msg)
        # cleanup stack
        BaseToDict._cleanup_stack(stack, value_converter, 0, strict)
        # end
        #return BaseToDict._finalize_root_dict(root_context, value_converter)
        return root_container

    @staticmethod
    def _prepare_line(line, context):
        indent_width = const.INDENT_WIDTH
        # empty or whitespace within Text context
        #if context.name in ("bin", "raw", "text"):
        if not line:
            return "", context.indents
        elif line.isspace():
            if len(line) <= context.indents * indent_width:
                return "", context.indents
            else:
                line = line[context.indents * indent_width:]
                return line, context.indents
        # unindent
        indents = misc.count_indents(line)
        line = line[indents * indent_width:]
        return line, indents

    @staticmethod
    def _process_line(line, stack, value_converter, strict):
        if not stack:
            return
        context = stack[-1]
        name = context.name
        collection = context.collection
        indents = context.indents
        if name == "bin":
            collection.append(line)
        elif name == "dict":
            # process comments
            if line.startswith("#"):
                if strict:
                    return
                comment_id = CommentID()
                collection[comment_id] = Comment(line)
            # process whitespaces
            elif not line or line.isspace():
                if strict:
                    return
                whitespace_id = WhitespaceID()
                collection[whitespace_id] = Whitespace()
            # process key value
            else:
                key, val = misc.split_key_value(line, sep="=", strip_whitespace=True)
                value = value_converter.decode(val)
                collection[key] = value
                container_name = BaseToDict._check_container_tag(val)
                if container_name:
                    BaseToDict._update_stack(stack, container_name, value, indents+1)
        elif name == "list":
            # process comments
            if line.startswith("#"):
                if strict:
                    return
                comment = Comment(line)
                collection.append(comment)
            # process whitespaces
            elif not line or line.isspace():
                if strict:
                    return
                whitespace = Whitespace(line)
                collection.append(whitespace)
            # process key value
            else:
                value = value_converter.decode(line)
                collection.append(value)
                container_name = BaseToDict._check_container_tag(line)
                if container_name:
                    BaseToDict._update_stack(stack, container_name, value, indents+1)
        elif name == "raw":
            collection.append(line)
        elif name == "text":
            collection.append(line)
        else:
            msg = "Unknown box '{}'. Expected bin, dict, list, text, or raw."
            msg = msg.format(name)
            raise errors.Error(msg)

    @staticmethod
    def _check_container_tag(value):
        if not value.startswith("(") or not value.endswith(")"):
            return None
        value = value.strip("()")
        if value not in ("bin", "dict", "list", "raw", "text"):
            return None
        return value

    @staticmethod
    def _update_stack(stack, container_name,
                      container, indents):
        new_context = Context(container_name, container, indents)
        stack.append(new_context)

    @staticmethod
    def _cleanup_stack(stack, value_converter, indents, strict):
        if not stack:
            return
        while True:
            if len(stack) == 1:
                break
            context = stack[-1]
            parent_context = stack[-2]
            if indents >= context.indents:
                break
            # bin
            if context.name == "bin":
                BaseToDict._finalize_bin(parent_context, context,
                                         value_converter, strict)
            # dict
            #elif context.name == "dict":
            #    BaseToDict._finalize_dict(parent_context, context,
            #                              value_converter)
            # list
            #elif context.name == "list":
            #    BaseToDict._finalize_list(parent_context, context,
            #                              value_converter)
            # raw
            elif context.name == "raw":
                BaseToDict._finalize_raw(parent_context, context,
                                         value_converter, strict)
            # text
            elif context.name == "text":
                BaseToDict._finalize_text(parent_context, context,
                                          value_converter, strict)
            # delete the latest context
            del stack[-1]

    @staticmethod
    def _finalize_root_dict(root_context, value_converter):
        default_dict_type = value_converter.dict_type
        collection = root_context.collection
        if type(collection) is default_dict_type:
            return collection
        return default_dict_type(collection)

    @staticmethod
    def _finalize_bin(parent_context, context, value_converter, strict):
        bin_block, whitespace_block = BaseToDict._split_block(context.collection)
        value = [item.strip() for item in bin_block if item]
        bin_data = value_converter.bin_decoder(value)
        #default_bin_type = value_converter.bin_type
        #if type(bin_data) is not default_bin_type:
        #    bin_data = default_bin_type(bin_data)
        BaseToDict._update_parent_context(parent_context, bin_data)
        for line in whitespace_block:
            BaseToDict._add_whitespace_to_parent_context(parent_context, line, strict)
    """
    @staticmethod
    def _finalize_dict(parent_context, context, value_converter):
        default_dict_type = value_converter.dict_type
        box = context.box
        if type(box) is default_dict_type:
            return
        box = default_dict_type(box)
        BaseToDict._update_parent_context(parent_context, box)

    @staticmethod
    def _finalize_list(parent_context, context, value_converter):
        default_raw_type = value_converter.list_type
        box = context.box
        if type(box) is default_raw_type:
            return
        box = default_raw_type(box)
        BaseToDict._update_parent_context(parent_context, box)
    """

    @staticmethod
    def _finalize_raw(parent_context, context, value_converter, strict):
        # concatenate text lines
        raw_block, whitespace_block = BaseToDict._split_block(context.collection)
        text = value_converter.raw_decoder(raw_block)

        #default_raw_type = value_converter.raw_type
        #if type(text) is not default_raw_type:
        #    text = default_raw_type(text)
        BaseToDict._update_parent_context(parent_context, text)
        for line in whitespace_block:
            BaseToDict._add_whitespace_to_parent_context(parent_context, line, strict)
        return
        #default_raw_type = value_converter.raw_type
        #box = context.box
        #if type(box) is default_raw_type:
        #    return
        #box = default_raw_type(box)
        #BaseToDict._update_parent_context(parent_context, box)

    @staticmethod
    def _finalize_text(parent_context, context, value_converter, strict):
        # concatenate text lines
        text_block, whitespace_block = BaseToDict._split_block(context.collection)
        text = value_converter.text_decoder(text_block)
        #default_text_type = value_converter.text_type
        #if type(text) is not default_text_type:
        #    text = default_text_type(text)
        BaseToDict._update_parent_context(parent_context, text)
        for line in whitespace_block:
            BaseToDict._add_whitespace_to_parent_context(parent_context, line, strict)

    @staticmethod
    def _split_block(block):
        x, y = block, list()
        for i, line in enumerate(reversed(block)):
            if line.rstrip() == "---":
                n = len(block)
                a = n - (i + 1)
                b = a + 1
                x, y = block[0:a], block[b:]
                break
        return x, y

    @staticmethod
    def _update_parent_context(parent_context, data):
        if parent_context.name == "dict":
            key = list(parent_context.collection.keys())[-1]
            parent_context.collection[key] = data
        elif parent_context.name == "list":
            parent_context.collection[-1] = data
        else:
            msg = "Invalid parent name '{}'"
            msg = msg.format(parent_context.name)
            raise errors.Error(msg)

    @staticmethod
    def _add_whitespace_to_parent_context(parent_context, data, strict):
        if strict:
            return
        whitespace = Whitespace(data)
        if parent_context.name == "dict":
            whitespace_id = WhitespaceID()
            parent_context.collection[whitespace_id] = whitespace
        elif parent_context.name == "list":
            parent_context.collection[-1] = whitespace
        else:
            msg = "Invalid parent name '{}'"
            msg = msg.format(parent_context.name)
            raise errors.Error(msg)


class DictToBase:
    @staticmethod
    def run(data, value_converter=None):
        value_converter = value_converter if value_converter else ValueConverter()
        if type(data) not in value_converter.dict_types:
            msg = "Expected: {}".format(", ".join(value_converter.dict_types))
            raise errors.Error(msg)
        return DictToBase._loop(data, value_converter)

    @staticmethod
    def _loop(data, value_converter, base=None, stack=None, cached_refs=None):
        base = base if base else list()
        cached_refs = cached_refs if cached_refs else list()
        cached_refs.append(data)
        if not stack:
            stack = list()
            #root_container = value_converter.dict_type()
            root_context = Context("dict", data, 0)
            stack.append(root_context)
        context = stack[-1]
        if context.name == "dict":
            DictToBase._handle_dict(context.collection, context,
                                    value_converter, base, stack,
                                    cached_refs)
        elif context.name == "list":
            DictToBase._handle_list(context.collection, context,
                                    value_converter, base, stack,
                                    cached_refs)
        return base

    @staticmethod
    def _handle_dict(data, context, value_converter, base, stack, cached_refs):
        indent_str = " " * const.INDENT_WIDTH
        context_indent_str = indent_str * context.indents
        for key, value in data.items():
            # comments
            if isinstance(key, CommentID):
                value = value.replace("\n", "\\n")
                base.append(context_indent_str + value)
            # whitespace
            elif isinstance(key, WhitespaceID):
                #base.append(context_indent_str + value)
                base.append(Whitespace())
            # Bin
            elif type(value) in value_converter.bin_types:
                line = "{} = (bin)".format(key)
                base.append(context_indent_str + line)
                result = value_converter.bin_encoder(value)
                for item in result:
                    line = context_indent_str + indent_str + item
                    base.append(line)
                #if result:
                line = context_indent_str + indent_str + "---"
                base.append(line)
            # Raw
            elif type(value) in value_converter.raw_types:
                line = "{} = (raw)".format(key)
                base.append(context_indent_str + line)
                result = value_converter.raw_encoder(value)
                for item in result:
                    line = context_indent_str + indent_str + item
                    base.append(line)
                #if result:
                line = context_indent_str + indent_str + "---"
                base.append(line)
            # Text
            elif type(value) in value_converter.text_types:
                line = "{} = (text)".format(key)
                base.append(context_indent_str + line)
                result = value_converter.text_encoder(value)
                for item in result:
                    line = context_indent_str + indent_str + item
                    base.append(line)
                #if result:
                line = context_indent_str + indent_str + "---"
                base.append(line)
            # list box
            elif type(value) in value_converter.list_types:
                #misc.update_cached_refs(value, cached_refs)
                result = value_converter.encode(value)
                line = "{} = {}".format(key, result)
                base.append(context_indent_str + line)
                new_context = Context("list", value, context.indents + 1)
                stack.append(new_context)
                DictToBase._loop(value, value_converter, base=base,
                                 stack=stack)
            # dict box
            elif type(value) in value_converter.dict_types:
                #misc.update_cached_refs(value, cached_refs)
                result = value_converter.encode(value)
                line = "{} = {}".format(key, result)
                base.append(context_indent_str + line)
                new_context = Context("dict", value, context.indents + 1)
                stack.append(new_context)
                DictToBase._loop(value, value_converter, base=base,
                                 stack=stack)
            # regular value (scalar, datetime, etc)
            else:
                key = key.replace("\n", "\\n")
                result = value_converter.encode(value)
                line = "{} = {}".format(key, result)
                base.append(context_indent_str + line)

    @staticmethod
    def _handle_list(data, context, value_converter, base, stack, cached_refs):
        indent_str = " " * const.INDENT_WIDTH
        context_indent_str = indent_str * context.indents
        for value in data:
            # comments
            if isinstance(value, Comment):
                value = value.replace("\n", "\\n")
                base.append(context_indent_str + value)
            # whitespace
            elif isinstance(value, Whitespace):
                #base.append(context_indent_str + value)
                base.append(Whitespace())
            # Bin
            elif type(value) in value_converter.bin_types:
                line = "(bin)"
                base.append(context_indent_str + line)
                result = value_converter.bin_encoder(value)
                for item in result:
                    line = context_indent_str + context_indent_str + item
                    base.append(line)
                #if result:
                line = context_indent_str + context_indent_str + "---"
                base.append(line)
            # Raw
            elif type(value) in value_converter.raw_types:
                line = "(raw)"
                base.append(context_indent_str + line)
                result = value_converter.raw_encoder(value)
                for item in result:
                    line = context_indent_str + context_indent_str + item
                    base.append(line)
                #if result:
                line = context_indent_str + context_indent_str + "---"
                base.append(line)
            # Text
            elif type(value) in value_converter.text_types:
                line = "(text)"
                base.append(context_indent_str + line)
                result = value_converter.text_encoder(value)
                for item in result:
                    line = context_indent_str + context_indent_str + item
                    base.append(line)
                #if result:
                line = context_indent_str + context_indent_str + "---"
                base.append(line)
            # list box
            elif type(value) in value_converter.list_types:
                #misc.update_cached_refs(value, cached_refs)
                result = value_converter.encode(value)
                base.append(context_indent_str + result)
                new_context = Context("list", value, context.indents + 1)
                stack.append(new_context)
                DictToBase._loop(value, value_converter, base=base,
                                 stack=stack)
            # dict box
            elif type(value) in value_converter.dict_types:
                #misc.update_cached_refs(value, cached_refs)
                result = value_converter.encode(value)
                base.append(context_indent_str + result)
                new_context = Context("dict", value, context.indents + 1)
                stack.append(new_context)
                DictToBase._loop(value, value_converter, base=base,
                                 stack=stack)
            # regular value (scalar, datetime, etc)
            else:
                result = value_converter.encode(value)
                base.append(context_indent_str + result)


Context = namedtuple("Context", ["name", "collection", "indents"])


class ValueConverter:
    """This class allows the developer to customize value encoding"""
    def __init__(self, dict_type=None, list_type=None,

                 dict_types=None, list_types=None,

                 bin_types=None, bool_types=None,
                 complex_types=None, date_types=None,
                 datetime_types=None, float_types=None,
                 integer_types=None, raw_types=None,
                 string_types=None, text_types=None,
                 time_types=None,

                 bin_encoder=None, bool_encoder=None,
                 complex_encoder=None, date_encoder=None,
                 datetime_encoder=None, float_encoder=None,
                 integer_encoder=None, null_encoder=None,
                 raw_encoder=None, string_encoder=None,
                 text_encoder=None, time_encoder=None,
                 fallback_encoder=None,

                 bin_decoder=None, bool_decoder=None,
                 complex_decoder=None, date_decoder=None,
                 datetime_decoder=None, float_decoder=None,
                 integer_decoder=None, null_decoder=None,
                 raw_decoder=None, string_decoder=None,
                 text_decoder=None, time_decoder=None,
                 fallback_decoder=None):
        """
        All parameters are mirrored with read and write properties

        [parameters]

        - dict_type: the Python type in which a Jesth Dict should be converted into. Defaults to Python dict type.

        - list_type: the Python type in which a Jesth List should be converted into. Defaults to Python list type.

        - XXX_types: this represents a group of parameters. Here, XXX is a placeholder for a Jesth data type. Valid types are: dict, list, bin, bool, complex, date, datetime, float, integer, raw, string, text, time. Examples: dict_types, float_types, and time_types. Use this parameter to set a list of Python types that may be encoded in the Jesth type (the same used as prefix). Example: dict_types defaults to [dict, OrderedDict], i.e., while encoding some Python data, an OrderedDict instance or a regular dict instance will be encoded as a Jesth dict.

        - XXX_encoder: this represents a group of parameters. Here, XXX is a placeholder for one of: bin, bool, complex, date, datetime, float, integer, null, raw, string, text, time, fallback. Use these parameters to set a callable to encode Python values into Jesth values. Example: float_encoder = decimal.Decimal

        - XXX_decoder: this represents a group of parameters. Here, XXX is a placeholder for one of: bin, bool, complex, date, datetime, float, integer, null, raw, string, text, time, fallback. Use these parameters to set a callable to decode Jesth values into Python values. Example: integer_decoder = int
        """

        # default types for dict and list containers
        self._dict_type = dict_type if dict_type else dict
        self._list_type = list_type if list_type else list

        # types for containers
        self._dict_types = dict_types if dict_types else [dict, OrderedDict]
        self._list_types = list_types if list_types else [list, tuple, set]

        # data types
        self._bin_types = bin_types if bin_types else [bytes]
        self._bool_types = bool_types if bool_types else [bool]
        self._complex_types = complex_types if complex_types else [complex]
        self._date_types = date_types if date_types else [datetime.date]
        self._datetime_types = datetime_types if datetime_types else [datetime.datetime]
        self._float_types = float_types if float_types else [float, Decimal]
        self._integer_types = integer_types if integer_types else [int, HexInt, OctInt, BinInt]
        self._raw_types = raw_types if raw_types else [RawText]
        self._string_types = string_types if string_types else [str, RawString]
        self._text_types = text_types if text_types else [Text]
        self._time_types = time_types if time_types else [datetime.time]

        # encoders
        self._bin_encoder = bin_encoder if bin_encoder else encode_bin
        self._bool_encoder = bool_encoder if bool_encoder else encode_bool
        self._complex_encoder = complex_encoder if complex_encoder else encode_complex
        self._date_encoder = date_encoder if date_encoder else encode_date
        self._datetime_encoder = datetime_encoder if datetime_encoder else encode_datetime
        self._float_encoder = float_encoder if float_encoder else encode_float
        self._integer_encoder = integer_encoder if integer_encoder else encode_integer
        self._null_encoder = null_encoder if null_encoder else encode_null
        self._raw_encoder = raw_encoder if raw_encoder else encode_raw
        self._string_encoder = string_encoder if string_encoder else encode_string
        self._text_encoder = text_encoder if text_encoder else encode_text
        self._time_encoder = time_encoder if time_encoder else encode_time
        self._fallback_encoder = fallback_encoder if fallback_encoder else encode_value

        # decoders
        self._bin_decoder = bin_decoder if bin_decoder else decode_bin
        self._bool_decoder = bool_decoder if bool_decoder else decode_bool
        self._complex_decoder = complex_decoder if complex_decoder else decode_complex
        self._date_decoder = date_decoder if date_decoder else decode_date
        self._datetime_decoder = datetime_decoder if datetime_decoder else decode_datetime
        self._float_decoder = float_decoder if float_decoder else decode_float
        self._integer_decoder = integer_decoder if integer_decoder else decode_integer
        self._null_decoder = null_decoder if null_decoder else decode_null
        self._raw_decoder = raw_decoder if raw_decoder else decode_raw
        self._string_decoder = string_decoder if string_decoder else decode_string
        self._text_decoder = text_decoder if text_decoder else decode_text
        self._time_decoder = time_decoder if time_decoder else decode_time
        self._fallback_decoder = fallback_decoder if fallback_decoder else decode_value

    # default types for containers

    @property
    def bin_type(self):
        return self._bin_type

    @bin_type.setter
    def bin_type(self, val):
        self._bin_type = val

    @property
    def dict_type(self):
        return self._dict_type

    @dict_type.setter
    def dict_type(self, val):
        self._dict_type = val

    @property
    def list_type(self):
        return self._list_type

    @list_type.setter
    def list_type(self, val):
        self._list_type = val

    @property
    def raw_type(self):
        return self._raw_type

    @raw_type.setter
    def raw_type(self, val):
        self._raw_type = val

    @property
    def text_type(self):
        return self._text_type

    @text_type.setter
    def text_type(self, val):
        self._text_type = val

    # types for containers

    @property
    def dict_types(self):
        return self._dict_types

    @dict_types.setter
    def dict_types(self, val):
        self._dict_types = val

    @property
    def list_types(self):
        return self._list_types

    @list_types.setter
    def list_types(self, val):
        self._list_types = val

    # types for values

    @property
    def bin_types(self):
        return self._bin_types

    @bin_types.setter
    def bin_types(self, val):
        self._bin_types = val

    @property
    def bool_types(self):
        return self._bool_types

    @bool_types.setter
    def bool_types(self, val):
        self._bool_types = val

    @property
    def complex_types(self):
        return self._complex_types

    @complex_types.setter
    def complex_types(self, val):
        self._complex_types = val

    @property
    def date_types(self):
        return self._date_types

    @date_types.setter
    def date_types(self, val):
        self._date_types = val

    @property
    def datetime_types(self):
        return self._datetime_types

    @datetime_types.setter
    def datetime_types(self, val):
        self._datetime_types = val

    @property
    def float_types(self):
        return self._float_types

    @float_types.setter
    def float_types(self, val):
        self._float_types = val

    @property
    def integer_types(self):
        return self._integer_types

    @integer_types.setter
    def integer_types(self, val):
        self._integer_types = val

    @property
    def raw_types(self):
        return self._raw_types

    @raw_types.setter
    def raw_types(self, val):
        self._raw_types = val

    @property
    def string_types(self):
        return self._string_types

    @string_types.setter
    def string_types(self, val):
        self._string_types = val

    @property
    def text_types(self):
        return self._text_types

    @text_types.setter
    def text_types(self, val):
        self._text_types = val

    @property
    def time_types(self):
        return self._time_types

    @time_types.setter
    def time_types(self, val):
        self._time_types = val

    # encoders

    @property
    def bin_encoder(self):
        return self._bin_encoder

    @bin_encoder.setter
    def bin_encoder(self, val):
        self._bin_encoder = val

    @property
    def bool_encoder(self):
        return self._bool_encoder

    @bool_encoder.setter
    def bool_encoder(self, val):
        self._bool_encoder = val

    @property
    def complex_encoder(self):
        return self._complex_encoder

    @complex_encoder.setter
    def complex_encoder(self, val):
        self._complex_encoder = val

    @property
    def date_encoder(self):
        return self._date_encoder

    @date_encoder.setter
    def date_encoder(self, val):
        self._date_encoder = val

    @property
    def datetime_encoder(self):
        return self._datetime_encoder

    @datetime_encoder.setter
    def datetime_encoder(self, val):
        self._datetime_encoder = val

    @property
    def dict_encoder(self):
        return self._dict_encoder

    @dict_encoder.setter
    def dict_encoder(self, val):
        self._dict_encoder = val

    @property
    def float_encoder(self):
        return self._float_encoder

    @float_encoder.setter
    def float_encoder(self, val):
        self._float_encoder = val

    @property
    def integer_encoder(self):
        return self._integer_encoder

    @integer_encoder.setter
    def integer_encoder(self, val):
        self._integer_encoder = val

    @property
    def list_encoder(self):
        return self._list_encoder

    @list_encoder.setter
    def list_encoder(self, val):
        self._list_encoder = val

    @property
    def null_encoder(self):
        return self._null_encoder

    @null_encoder.setter
    def null_encoder(self, val):
        self._null_encoder = val

    @property
    def raw_encoder(self):
        return self._raw_encoder

    @raw_encoder.setter
    def raw_encoder(self, val):
        self._raw_encoder = val

    @property
    def string_encoder(self):
        return self._string_encoder

    @string_encoder.setter
    def string_encoder(self, val):
        self._string_encoder = val

    @property
    def text_encoder(self):
        return self._text_encoder

    @text_encoder.setter
    def text_encoder(self, val):
        self._text_encoder = val

    @property
    def time_encoder(self):
        return self._time_encoder

    @time_encoder.setter
    def time_encoder(self, val):
        self._time_encoder = val     
            
    @property
    def fallback_encoder(self):
        return self._fallback_encoder

    @fallback_encoder.setter
    def fallback_encoder(self, val):
        self._fallback_encoder = val

    # decoders

    @property
    def bin_decoder(self):
        return self._bin_decoder

    @bin_decoder.setter
    def bin_decoder(self, val):
        self._bin_decoder = val

    @property
    def bool_decoder(self):
        return self._bool_decoder

    @bool_decoder.setter
    def bool_decoder(self, val):
        self._bool_decoder = val

    @property
    def complex_decoder(self):
        return self._complex_decoder

    @complex_decoder.setter
    def complex_decoder(self, val):
        self._complex_decoder = val

    @property
    def date_decoder(self):
        return self._date_decoder

    @date_decoder.setter
    def date_decoder(self, val):
        self._date_decoder = val

    @property
    def datetime_decoder(self):
        return self._datetime_decoder

    @datetime_decoder.setter
    def datetime_decoder(self, val):
        self._datetime_decoder = val

    @property
    def dict_decoder(self):
        return self._dict_decoder

    @dict_decoder.setter
    def dict_decoder(self, val):
        self._dict_decoder = val

    @property
    def float_decoder(self):
        return self._float_decoder

    @float_decoder.setter
    def float_decoder(self, val):
        self._float_decoder = val

    @property
    def integer_decoder(self):
        return self._integer_decoder

    @integer_decoder.setter
    def integer_decoder(self, val):
        self._integer_decoder = val

    @property
    def list_decoder(self):
        return self._list_decoder

    @list_decoder.setter
    def list_decoder(self, val):
        self._list_decoder = val

    @property
    def null_decoder(self):
        return self._null_decoder

    @null_decoder.setter
    def null_decoder(self, val):
        self._null_decoder = val

    @property
    def raw_decoder(self):
        return self._raw_decoder

    @raw_decoder.setter
    def raw_decoder(self, val):
        self._raw_decoder = val

    @property
    def string_decoder(self):
        return self._string_decoder

    @string_decoder.setter
    def string_decoder(self, val):
        self._string_decoder = val

    @property
    def text_decoder(self):
        return self._text_decoder

    @text_decoder.setter
    def text_decoder(self, val):
        self._text_decoder = val

    @property
    def time_decoder(self):
        return self._time_decoder

    @time_decoder.setter
    def time_decoder(self, val):
        self._time_decoder = val

    @property
    def fallback_decoder(self):
        return self._fallback_decoder

    @fallback_decoder.setter
    def fallback_decoder(self, val):
        self._fallback_decoder = val

    def encode(self, value):
        # box
        container_tag = self._encode_container(value)
        if container_tag:
            return container_tag
        # null
        if value is None:
            return self._null_encoder(value)
        # == data types
        value_type = type(value)
        # bool
        if value_type in self._bool_types:
            return self._bool_encoder(value)
        # complex
        if value_type in self._complex_types:
            return self._complex_encoder(value)
        # date
        if value_type in self._date_types:
            return self._date_encoder(value)
        # datetime
        if value_type in self._datetime_types:
            return self._datetime_encoder(value)
        # float
        if value_type in self._float_types:
            return self._float_encoder(value)
        # integer
        if value_type in self._integer_types:
            return self._integer_encoder(value)
        # string
        if value_type in self._string_types:
            return self._string_encoder(value)
        # time
        if value_type in self._time_types:
            return self._time_encoder(value)
        # default
        return self._fallback_encoder(value)

    def decode(self, value):
        value = value.strip()
        container = self._decode_container(value)
        if container is not None:
            return container
        # scalars and co.  (note that the order of items matters here)
        decoders = (self._null_decoder, self._bool_decoder,
                    self._string_decoder, self._complex_decoder,
                    self._integer_decoder, self._float_decoder,
                    self._date_decoder, self._time_decoder,
                    self._datetime_decoder, self._fallback_decoder)
        for p in decoders:
            try:
                result = p(value)
            except Exception as e:
                continue
            else:
                return result
        raise errors.ConversionError

    def _encode_container(self, val):
        value_type = type(val)
        # bin
        if value_type in self._bin_types:
            return "(bin)"
        # dict
        if value_type in self._dict_types:
            return "(dict)"
        # list
        if value_type in self._list_types:
            return "(list)"
        # raw
        if value_type in self._raw_types:
            return "(raw)"
        # text
        if value_type in self._text_types:
            return "(text)"
        return None

    def _decode_container(self, val):
        if not val.startswith("(") or not val.endswith(")"):
            return None
        # bin
        if val == "(bin)":
            return list()
        # dict
        if val == "(dict)":
            return self._dict_type()
        # list
        if val == "(list)":
            return self._list_type()
        # raw
        if val == "(raw)":
            return list()
        # text
        if val == "(text)":
            return list()
        msg = "Expected one of these containers: (bin), (dict), (list), (raw), (text)"
        raise errors.Error(msg)


# === Encoders ===

def encode_bin(val):
    if not val:
        return list()
    r = base64.standard_b64encode(val)
    r = r.decode("utf-8")
    r = r.replace("\n", "")
    result = list()
    cache = list()
    i = 0
    for char in r:
        if i == 76:
            i = 0
            result.append("".join(cache))
            cache = list()
            cache.append(char)
            continue
        cache.append(char)
        i += 1
    if cache:
        result.append("".join(cache))
    return result
    

def encode_bool(val):
    if val:
        return "true"
    return "false"


def encode_complex(val):
    real, imag = val.real, val.imag
    real = int(real) if real.is_integer() else real
    imag = int(imag) if imag.is_integer() else imag
    tidy_real = misc.tidy_up_float(real)
    tidy_imag = misc.tidy_up_float(imag)
    return "{}{}{}i".format(tidy_real, "" if imag < 0 else "+", tidy_imag)


def encode_date(val):
    """Parse date and time with the ISO 8601 format"""
    # date ISO format
    return str(val)


def encode_datetime(val):
    value = val.isoformat()
    if value.endswith("+00:00"):
        value = value.replace("+00:00", "Z")
    return str(value)


def encode_float(val):
    if isinstance(val, Decimal):
        val = "{:E}".format(val)
    return misc.tidy_up_float(val)


def encode_integer(val):
    t = type(val)
    if t is int:
        return misc.tidy_up_int(val)
    if t is HexInt:
        return misc.tidy_up_hex(hex(val))
    if t is OctInt:
        return misc.tidy_up_oct(oct(val))
    if t is BinInt:
        return misc.tidy_up_bin(bin(val))
    return str(val)


def encode_null(val):
    return "null"


def encode_raw(val):
    if not val:
        return list()
    return val.split("\n")


def encode_string(val):
    t = type(val)
    # raw string (literal)
    if t is RawString:
        val = val.replace("\n", "\\n")
        return "'{}'".format(val)
    # processed string
    val = val.replace("\\", "\\\\")
    val = val.replace("\n", "\\n")
    return '"{}"'.format(val)


def encode_text(val):
    if not val:
        return list()
    val = val.replace("\\", "\\\\")
    return val.split("\n")


def encode_time(val):
    # time ISO format
    return str(val)


def encode_value(val):
    return encode_string(str(val))


# === Decoders ===


def decode_bin(val):
    # list of strings
    val = "".join(val)
    return base64.standard_b64decode(val)


def decode_bool(val):
    val = val.lower()
    if val == "true":
        return bool(1)
    elif val == "false":
        return bool(0)
    raise errors.ConversionError


def decode_complex(val):
    if val.endswith("i"):
        val = val.replace(" ", "")
        val = val.rstrip("i") + "j"
        return complex(val)
    raise errors.ConversionError


def decode_date(val):
    """Parse date and time with the ISO 8601 format"""
    # date ISO format
    return datetime.date.fromisoformat(val)


def decode_datetime(val):
    # datetime (2023-03-13T09:10:42Z)
    if val.endswith("Z"):
        val += "+00:00"
    return datetime.datetime.fromisoformat(val)


def decode_float(val):
    if "e" in val.lower():
        return Decimal(val)
    if "." in val:
        return float(val)
    raise errors.ConversionError


def decode_integer(val):
    v = val.lstrip("+-")
    # hexadecimal
    if v.startswith("0x"):
        val = int(val, 16)
        return HexInt(val)
    # octal
    if v.startswith("0o"):
        val = int(val, 8)
        return OctInt(val)
    # binary
    if v.startswith("0b"):
        val = int(val, 2)
        return BinInt(val)
    # default base 10
    return int(val)


def decode_null(val):
    val = val.lower()
    if val == "null":
        return None
    raise errors.ConversionError


def decode_raw(val):
    # val is a list of string
    text = "\n".join(val)
    return RawText(text)


def decode_string(val):
    if val.startswith('"') and val.endswith('"'):
        return misc.decode_unicode(val[1:-1])
    if val.startswith("'") and val.endswith("'"):
        return RawString(val[1:-1])
    raise errors.ConversionError
    #val = misc.replace_newlines(val)
    #val = misc.replace_tabs(val)


def decode_text(val):
    text = "\n".join(val)
    text = misc.decode_unicode(text)
    return Text(text)


def decode_time(val):
    # time ISO format
    return datetime.time.fromisoformat(val)


def decode_value(val):
    raise errors.ConversionError
