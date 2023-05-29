Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.converter**
 
Classes and functions to convert a section body into a Python dict, or flatten a Python dict into a section body

> **Classes:** &nbsp; [BaseToDict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/BaseToDict.md#class-basetodict) &nbsp;&nbsp; [Context](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/Context.md#class-context) &nbsp;&nbsp; [DictToBase](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/DictToBase.md#class-dicttobase) &nbsp;&nbsp; [ValueConverter](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/ValueConverter.md#class-valueconverter)
>
> **Functions:** &nbsp; [create\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#create_dict) &nbsp;&nbsp; [decode\_bin](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_bin) &nbsp;&nbsp; [decode\_bool](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_bool) &nbsp;&nbsp; [decode\_complex](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_complex) &nbsp;&nbsp; [decode\_date](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_date) &nbsp;&nbsp; [decode\_datetime](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_datetime) &nbsp;&nbsp; [decode\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_float) &nbsp;&nbsp; [decode\_integer](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_integer) &nbsp;&nbsp; [decode\_null](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_null) &nbsp;&nbsp; [decode\_raw](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_raw) &nbsp;&nbsp; [decode\_string](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_string) &nbsp;&nbsp; [decode\_text](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_text) &nbsp;&nbsp; [decode\_time](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_time) &nbsp;&nbsp; [decode\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_value) &nbsp;&nbsp; [encode\_bin](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_bin) &nbsp;&nbsp; [encode\_bool](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_bool) &nbsp;&nbsp; [encode\_complex](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_complex) &nbsp;&nbsp; [encode\_date](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_date) &nbsp;&nbsp; [encode\_datetime](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_datetime) &nbsp;&nbsp; [encode\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_float) &nbsp;&nbsp; [encode\_integer](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_integer) &nbsp;&nbsp; [encode\_null](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_null) &nbsp;&nbsp; [encode\_raw](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_raw) &nbsp;&nbsp; [encode\_string](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_string) &nbsp;&nbsp; [encode\_text](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_text) &nbsp;&nbsp; [encode\_time](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_time) &nbsp;&nbsp; [encode\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_value) &nbsp;&nbsp; [flatten\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#flatten_dict)
>
> **Constants:** &nbsp; None

# Class ValueConverter
This class allows the developer to customize value encoding

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|bin_decoder|getter|None||
|bin_decoder|setter|None||
|bin_encoder|getter|None||
|bin_encoder|setter|None||
|bin_type|getter|None||
|bin_type|setter|None||
|bin_types|getter|None||
|bin_types|setter|None||
|bool_decoder|getter|None||
|bool_decoder|setter|None||
|bool_encoder|getter|None||
|bool_encoder|setter|None||
|bool_types|getter|None||
|bool_types|setter|None||
|complex_decoder|getter|None||
|complex_decoder|setter|None||
|complex_encoder|getter|None||
|complex_encoder|setter|None||
|complex_types|getter|None||
|complex_types|setter|None||
|date_decoder|getter|None||
|date_decoder|setter|None||
|date_encoder|getter|None||
|date_encoder|setter|None||
|date_types|getter|None||
|date_types|setter|None||
|datetime_decoder|getter|None||
|datetime_decoder|setter|None||
|datetime_encoder|getter|None||
|datetime_encoder|setter|None||
|datetime_types|getter|None||
|datetime_types|setter|None||
|dict_decoder|getter|None||
|dict_decoder|setter|None||
|dict_encoder|getter|None||
|dict_encoder|setter|None||
|dict_type|getter|None||
|dict_type|setter|None||
|dict_types|getter|None||
|dict_types|setter|None||
|fallback_decoder|getter|None||
|fallback_decoder|setter|None||
|fallback_encoder|getter|None||
|fallback_encoder|setter|None||
|float_decoder|getter|None||
|float_decoder|setter|None||
|float_encoder|getter|None||
|float_encoder|setter|None||
|float_types|getter|None||
|float_types|setter|None||
|integer_decoder|getter|None||
|integer_decoder|setter|None||
|integer_encoder|getter|None||
|integer_encoder|setter|None||
|integer_types|getter|None||
|integer_types|setter|None||
|list_decoder|getter|None||
|list_decoder|setter|None||
|list_encoder|getter|None||
|list_encoder|setter|None||
|list_type|getter|None||
|list_type|setter|None||
|list_types|getter|None||
|list_types|setter|None||
|null_decoder|getter|None||
|null_decoder|setter|None||
|null_encoder|getter|None||
|null_encoder|setter|None||
|raw_decoder|getter|None||
|raw_decoder|setter|None||
|raw_encoder|getter|None||
|raw_encoder|setter|None||
|raw_type|getter|None||
|raw_type|setter|None||
|raw_types|getter|None||
|raw_types|setter|None||
|string_decoder|getter|None||
|string_decoder|setter|None||
|string_encoder|getter|None||
|string_encoder|setter|None||
|string_types|getter|None||
|string_types|setter|None||
|text_decoder|getter|None||
|text_decoder|setter|None||
|text_encoder|getter|None||
|text_encoder|setter|None||
|text_type|getter|None||
|text_type|setter|None||
|text_types|getter|None||
|text_types|setter|None||
|time_decoder|getter|None||
|time_decoder|setter|None||
|time_encoder|getter|None||
|time_encoder|setter|None||
|time_types|getter|None||
|time_types|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [decode](#decode) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [\_decode\_container](#_decode_container) &nbsp;&nbsp; [\_encode\_container](#_encode_container)

## \_\_init\_\_
All parameters are mirrored with read and write properties



**Signature:** (self, dict\_type=None, list\_type=None, dict\_types=None, list\_types=None, bin\_types=None, bool\_types=None, complex\_types=None, date\_types=None, datetime\_types=None, float\_types=None, integer\_types=None, raw\_types=None, string\_types=None, text\_types=None, time\_types=None, bin\_encoder=None, bool\_encoder=None, complex\_encoder=None, date\_encoder=None, datetime\_encoder=None, float\_encoder=None, integer\_encoder=None, null\_encoder=None, raw\_encoder=None, string\_encoder=None, text\_encoder=None, time\_encoder=None, fallback\_encoder=None, bin\_decoder=None, bool\_decoder=None, complex\_decoder=None, date\_decoder=None, datetime\_decoder=None, float\_decoder=None, integer\_decoder=None, null\_decoder=None, raw\_decoder=None, string\_decoder=None, text\_decoder=None, time\_decoder=None, fallback\_decoder=None)

|Parameter|Description|
|---|---|
|dict\_type|the Python type in which a Jesth Dict should be converted into. Defaults to Python dict type. |
|list\_type|the Python type in which a Jesth List should be converted into. Defaults to Python list type. |
|XXX\_types|this represents a group of parameters. Here, XXX is a placeholder for a Jesth data type. Valid types are: dict, list, bin, bool, complex, date, datetime, float, integer, raw, string, text, time. Examples: dict_types, float_types, and time_types. Use this parameter to set a list of Python types that may be encoded in the Jesth type (the same used as prefix). Example: dict_types defaults to [dict, OrderedDict], i.e., while encoding some Python data, an OrderedDict instance or a regular dict instance will be encoded as a Jesth dict. |
|XXX\_encoder|this represents a group of parameters. Here, XXX is a placeholder for one of: bin, bool, complex, date, datetime, float, integer, null, raw, string, text, time, fallback. Use these parameters to set a callable to encode Python values into Jesth values. Example: float_encoder = decimal.Decimal |
|XXX\_decoder|this represents a group of parameters. Here, XXX is a placeholder for one of: bin, bool, complex, date, datetime, float, integer, null, raw, string, text, time, fallback. Use these parameters to set a callable to decode Jesth values into Python values. Example: integer_decoder = int|





**Return Value:** None

[Back to Top](#module-overview)


## decode
No description



**Signature:** (self, value)





**Return Value:** None

[Back to Top](#module-overview)


## encode
No description



**Signature:** (self, value)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_container
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_container
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)



