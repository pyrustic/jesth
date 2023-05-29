Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.converter**
 
Classes and functions to convert a section body into a Python dict, or flatten a Python dict into a section body

> **Classes:** &nbsp; [BaseToDict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/BaseToDict.md#class-basetodict) &nbsp;&nbsp; [Context](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/Context.md#class-context) &nbsp;&nbsp; [DictToBase](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/DictToBase.md#class-dicttobase) &nbsp;&nbsp; [ValueConverter](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.converter/content/classes/ValueConverter.md#class-valueconverter)
>
> **Functions:** &nbsp; [create\_dict](#create_dict) &nbsp;&nbsp; [decode\_bin](#decode_bin) &nbsp;&nbsp; [decode\_bool](#decode_bool) &nbsp;&nbsp; [decode\_complex](#decode_complex) &nbsp;&nbsp; [decode\_date](#decode_date) &nbsp;&nbsp; [decode\_datetime](#decode_datetime) &nbsp;&nbsp; [decode\_float](#decode_float) &nbsp;&nbsp; [decode\_integer](#decode_integer) &nbsp;&nbsp; [decode\_null](#decode_null) &nbsp;&nbsp; [decode\_raw](#decode_raw) &nbsp;&nbsp; [decode\_string](#decode_string) &nbsp;&nbsp; [decode\_text](#decode_text) &nbsp;&nbsp; [decode\_time](#decode_time) &nbsp;&nbsp; [decode\_value](#decode_value) &nbsp;&nbsp; [encode\_bin](#encode_bin) &nbsp;&nbsp; [encode\_bool](#encode_bool) &nbsp;&nbsp; [encode\_complex](#encode_complex) &nbsp;&nbsp; [encode\_date](#encode_date) &nbsp;&nbsp; [encode\_datetime](#encode_datetime) &nbsp;&nbsp; [encode\_float](#encode_float) &nbsp;&nbsp; [encode\_integer](#encode_integer) &nbsp;&nbsp; [encode\_null](#encode_null) &nbsp;&nbsp; [encode\_raw](#encode_raw) &nbsp;&nbsp; [encode\_string](#encode_string) &nbsp;&nbsp; [encode\_text](#encode_text) &nbsp;&nbsp; [encode\_time](#encode_time) &nbsp;&nbsp; [encode\_value](#encode_value) &nbsp;&nbsp; [flatten\_dict](#flatten_dict)
>
> **Constants:** &nbsp; None

# All Functions
[create\_dict](#create_dict) &nbsp;&nbsp; [decode\_bin](#decode_bin) &nbsp;&nbsp; [decode\_bool](#decode_bool) &nbsp;&nbsp; [decode\_complex](#decode_complex) &nbsp;&nbsp; [decode\_date](#decode_date) &nbsp;&nbsp; [decode\_datetime](#decode_datetime) &nbsp;&nbsp; [decode\_float](#decode_float) &nbsp;&nbsp; [decode\_integer](#decode_integer) &nbsp;&nbsp; [decode\_null](#decode_null) &nbsp;&nbsp; [decode\_raw](#decode_raw) &nbsp;&nbsp; [decode\_string](#decode_string) &nbsp;&nbsp; [decode\_text](#decode_text) &nbsp;&nbsp; [decode\_time](#decode_time) &nbsp;&nbsp; [decode\_value](#decode_value) &nbsp;&nbsp; [encode\_bin](#encode_bin) &nbsp;&nbsp; [encode\_bool](#encode_bool) &nbsp;&nbsp; [encode\_complex](#encode_complex) &nbsp;&nbsp; [encode\_date](#encode_date) &nbsp;&nbsp; [encode\_datetime](#encode_datetime) &nbsp;&nbsp; [encode\_float](#encode_float) &nbsp;&nbsp; [encode\_integer](#encode_integer) &nbsp;&nbsp; [encode\_null](#encode_null) &nbsp;&nbsp; [encode\_raw](#encode_raw) &nbsp;&nbsp; [encode\_string](#encode_string) &nbsp;&nbsp; [encode\_text](#encode_text) &nbsp;&nbsp; [encode\_time](#encode_time) &nbsp;&nbsp; [encode\_value](#encode_value) &nbsp;&nbsp; [flatten\_dict](#flatten_dict)

## create\_dict
Convert a section body into a Python dict



**Signature:** (body, value\_converter=None, strict=True)

|Parameter|Description|
|---|---|
|body|string or list of strings|
|value\_converter|instance of ValueConverter to customize value encoding|
|strict|when strict is True, comments and whitespaces aren't preserved|



|Exception|Description|
|---|---|
|jesth.error.ConversionError|raised when an error occured while doing conversion|



**Return Value:** Returns a Python dict (type customizable with ValueConverter)

[Back to Top](#module-overview)


## decode\_bin
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_bool
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_complex
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_date
Parse date and time with the ISO 8601 format



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_datetime
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_float
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_integer
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_null
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_raw
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_string
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_text
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_time
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_value
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_bin
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_bool
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_complex
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_date
Parse date and time with the ISO 8601 format



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_datetime
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_float
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_integer
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_null
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_raw
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_string
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_text
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_time
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_value
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## flatten\_dict
Convert a Python dict into a list of strings (section body in the base form)



**Signature:** (data, value\_converter=None)

|Parameter|Description|
|---|---|
|data|Python dict|
|value\_converter|instance of ValueConverter to customize value encoding|





**Return Value:** Returns a list of strings

[Back to Top](#module-overview)


