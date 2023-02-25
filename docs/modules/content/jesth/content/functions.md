Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth**
 
This module exposes the API of this library

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [get\_key\_value](#get_key_value) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [write](#write)
>
> **Constants:** &nbsp; None

# All Functions
[get\_key\_value](#get_key_value) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [write](#write)

## get\_key\_value
Split a string into key and value parts.
The string must have a separator defined as an argument.
By default, the separator is ":".
An example of a valid string is "name: John Doe ".
The result will be: ("name": "John Doe")




**Signature:** (line, sep='=', strip\_whitespace=True)

|Parameter|Description|
|---|---|
|line|the string to split|
|sep|the separator, by default it is ":"|
|strip\_whitespace|boolean to tell whether you want whitespace to be stripped out or not. By default, the value is True. |





**Return Value:** Always returns a tuple. If the key doesn't exist, it will be an empty string

[Back to Top](#module-overview)


## parse
Parse a text, return a Jesth structure




**Signature:** (text, compact=False, split\_body=True)

|Parameter|Description|
|---|---|
|source|Source is either a text or a pathlib.Path object|
|compact|boolean to tell if whether you want whitespace and empty lines to be stripped or not. By default, empty lines and whitespaces are kept.|
|split\_body|boolean to tell if you want the body to be splitted as a list of string |





**Return Value:** Returns a Jesth structure. A Jesth structure is a dict.
Each key represents a section title.
The value of a key is the body of the section.
The body is a list of string, each string represents a line of text without the newline at end.

[Back to Top](#module-overview)


## read
Parse a file, return a Jesth structure




**Signature:** (source, compact=False, split\_body=True)

|Parameter|Description|
|---|---|
|source|Source is either a path or a pathlib.Path object|
|compact|boolean to tell if whether you want empty lines to be stripped or not. By default, empty lines are kept.|
|split\_body|boolean to tell if you want the body to be splitted as a list of string |





**Return Value:** Returns a Jesth structure. A Jesth structure is a dict.
Each key represents a section title.
The value of a key is the body of the section.
The body is a list of string, each string represents a line of text without the newline at end.

[Back to Top](#module-overview)


## render
Convert a Jesth structure into plain text




**Signature:** (structure)

|Parameter|Description|
|---|---|
|structure|dict, Jesth structure. Each key represents a section title. The value of a key is the body of the section. The body is either a string (with newlines or none), or a list of strings |



|Exception|Description|
|---|---|
|jesth.error.StructureError|raised if the structure isn't valid |



**Return Value:** Return the rendered plain text

[Back to Top](#module-overview)


## write
Convert a Jesth structure into plain text then save it in a file (the parent directory should exist)




**Signature:** (structure, destination)

|Parameter|Description|
|---|---|
|structure|dict, Jesth structure. Each key represents a section title. The value of a key is the body of the section. The body is either a string (with newlines or none), or a list of strings|
|destination|str, the path (or a pathlib.Path instance) to a file in which the rendered Jesth text can be saved. |



|Exception|Description|
|---|---|
|jesth.error.StructureError|raised if the structure isn't valid |



**Return Value:** Return the rendered plain text

[Back to Top](#module-overview)


