Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.converter**
 
Classes and functions to convert a section body into a Python dict, or flatten a Python dict into a section body

> **Classes:** &nbsp; [BaseToDict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/BaseToDict.md#class-basetodict) &nbsp;&nbsp; [Context](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/Context.md#class-context) &nbsp;&nbsp; [DictToBase](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/DictToBase.md#class-dicttobase) &nbsp;&nbsp; [ValueConverter](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/ValueConverter.md#class-valueconverter)
>
> **Functions:** &nbsp; [create\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#create_dict) &nbsp;&nbsp; [decode\_bin](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_bin) &nbsp;&nbsp; [decode\_bool](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_bool) &nbsp;&nbsp; [decode\_complex](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_complex) &nbsp;&nbsp; [decode\_date](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_date) &nbsp;&nbsp; [decode\_datetime](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_datetime) &nbsp;&nbsp; [decode\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_float) &nbsp;&nbsp; [decode\_integer](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_integer) &nbsp;&nbsp; [decode\_null](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_null) &nbsp;&nbsp; [decode\_raw](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_raw) &nbsp;&nbsp; [decode\_string](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_string) &nbsp;&nbsp; [decode\_text](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_text) &nbsp;&nbsp; [decode\_time](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_time) &nbsp;&nbsp; [decode\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#decode_value) &nbsp;&nbsp; [encode\_bin](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_bin) &nbsp;&nbsp; [encode\_bool](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_bool) &nbsp;&nbsp; [encode\_complex](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_complex) &nbsp;&nbsp; [encode\_date](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_date) &nbsp;&nbsp; [encode\_datetime](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_datetime) &nbsp;&nbsp; [encode\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_float) &nbsp;&nbsp; [encode\_integer](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_integer) &nbsp;&nbsp; [encode\_null](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_null) &nbsp;&nbsp; [encode\_raw](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_raw) &nbsp;&nbsp; [encode\_string](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_string) &nbsp;&nbsp; [encode\_text](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_text) &nbsp;&nbsp; [encode\_time](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_time) &nbsp;&nbsp; [encode\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#encode_value) &nbsp;&nbsp; [flatten\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/functions.md#flatten_dict)
>
> **Constants:** &nbsp; None

# Class Context
Context(name, collection, indents)

## Base Classes
tuple

## Class Attributes
\_field\_defaults &nbsp;&nbsp; \_fields &nbsp;&nbsp; \_fields\_defaults &nbsp;&nbsp; \_make &nbsp;&nbsp; collection &nbsp;&nbsp; indents &nbsp;&nbsp; name

## Class Properties


# All Methods
[count](#count) &nbsp;&nbsp; [index](#index) &nbsp;&nbsp; [\_asdict](#_asdict) &nbsp;&nbsp; [\_replace](#_replace)

## count
Return number of occurrences of value.

**Inherited from:** tuple

**Signature:** (self, value, /)





**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** tuple

**Signature:** (self, value, start=0, stop=9223372036854775807, /)





**Return Value:** None

[Back to Top](#module-overview)


## \_asdict
Return a new dict which maps field names to their values.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_replace
Return a new Context object replacing specified fields with new values



**Signature:** (self, /, \*\*kwds)





**Return Value:** None

[Back to Top](#module-overview)



