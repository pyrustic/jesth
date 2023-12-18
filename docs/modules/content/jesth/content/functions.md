Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth**
 
For convenience, this module exposes main classes and functions of the library

> **Classes:** &nbsp; [Document](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Document.md#class-document) &nbsp;&nbsp; [Parser](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Parser.md#class-parser) &nbsp;&nbsp; [Section](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Section.md#class-section) &nbsp;&nbsp; [ValueConverter](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/ValueConverter.md#class-valueconverter)
>
> **Functions:** &nbsp; [create\_dict](#create_dict) &nbsp;&nbsp; [decode](#decode) &nbsp;&nbsp; [deserialize](#deserialize) &nbsp;&nbsp; [dump](#dump) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [flatten\_dict](#flatten_dict) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [serialize](#serialize) &nbsp;&nbsp; [split\_key\_value](#split_key_value) &nbsp;&nbsp; [write](#write) &nbsp;&nbsp; [write\_to\_file](#write_to_file)
>
> **Constants:** &nbsp; None

# All Functions
[create\_dict](#create_dict) &nbsp;&nbsp; [decode](#decode) &nbsp;&nbsp; [deserialize](#deserialize) &nbsp;&nbsp; [dump](#dump) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [flatten\_dict](#flatten_dict) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [serialize](#serialize) &nbsp;&nbsp; [split\_key\_value](#split_key_value) &nbsp;&nbsp; [write](#write) &nbsp;&nbsp; [write\_to\_file](#write_to_file)

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
|jesth.errors.ConversionError|raised when an errors occured while doing conversion|



**Return Value:** Returns a Python dict (type customizable with ValueConverter)

[Back to Top](#module-overview)


## decode
No description



**Signature:** (text, value\_converter=None)





**Return Value:** None

[Back to Top](#module-overview)


## deserialize
No description



**Signature:** (raw, value\_converter=None)





**Return Value:** None

[Back to Top](#module-overview)


## dump
No description



**Signature:** (data, destination, value\_converter=None)





**Return Value:** None

[Back to Top](#module-overview)


## encode
No description



**Signature:** (data, value\_converter=None)





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


## load
Load data from a file or file object



**Signature:** (source, value\_converter=None)





**Return Value:** None

[Back to Top](#module-overview)


## parse
Parse a text, return a document



**Signature:** (text, value\_converter=None)

|Parameter|Description|
|---|---|
|text|text string|
|value\_converter|instance of jesth.converter.ValueConverter to customize value encoding|





**Return Value:** Returns an instance of jesth.document.Document

[Back to Top](#module-overview)


## read
Read a file, returns a document (jesth.document.Document)



**Signature:** (source, value\_converter=None)

|Parameter|Description|
|---|---|
|source|source is either a path string or a pathlib.Path object, or a binary file-like object|
|value\_converter|instance of jesth.converter.ValueConverter to customize value encoding|





**Return Value:** Returns an instance of jesth.document.Document

[Back to Top](#module-overview)


## render
Convert a jesth document into plain text



**Signature:** (document, \*headers, spacing=1)

|Parameter|Description|
|---|---|
|document|an instance of jesth.document.Document|
|\*headers|Headers of sections to render. Omitting this will render the entire section|
|spacing|number of empty lines between two adjacent sections. Defaults to 1 empty line.|





**Return Value:** Returns a string that contains sections (each made of square-brackets
delimited header and associated body). This string can be stored in a file,
thus creating a JesthFile

[Back to Top](#module-overview)


## serialize
No description



**Signature:** (data, value\_converter=None)





**Return Value:** None

[Back to Top](#module-overview)


## split\_key\_value
Split a line (string) into key and value parts.
The string must have a separator (defaults to "=").
An example of a valid string is "name = John Doe ".
The return will be: ("name": "John Doe")



**Signature:** (line, sep='=', strip\_whitespace=True)

|Parameter|Description|
|---|---|
|line|the string to split|
|sep|the separator, by default it is "="|
|strip\_whitespace|boolean to tell whether you want whitespace at each side of the key and value to be stripped out or not. By default, the value is True.|



|Exception|Description|
|---|---|
|errors.Error|if the separator, the key, or the value is missing,|



**Return Value:** Returns a ("key", "value") tuple if everything is Ok

[Back to Top](#module-overview)


## write
Convert a jesth document into plain text then write it in a file



**Signature:** (document, destination)

|Parameter|Description|
|---|---|
|document|an instance of jesth.document.Document|
|destination|path string, or pathlib.Path instance to a file in which the rendered Jesth text can be saved.|





**Return Value:** Returns the rendered plain text

[Back to Top](#module-overview)


## write\_to\_file
Write to a file (TRY to do it atomically for GNU/Linux and MacOS)
Check https://danluu.com/file-consistency/



**Signature:** (data, dest)

|Parameter|Description|
|---|---|
|data|str, data to write to file|
|dest|a pathlib.Path instance, or a path string|
|binary\_mode|boolean to tell if data should be written in dest with binary mode on (mode="wb")|
|encoding|defaults to "utf-8" and automatically set to None when binary mode is True|





**Return Value:** None

[Back to Top](#module-overview)


