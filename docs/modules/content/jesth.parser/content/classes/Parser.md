Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.parser**
 
This module exposes read and parse functions that return a document instance

> **Classes:** &nbsp; [Parser](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.parser/content/classes/Parser.md#class-parser)
>
> **Functions:** &nbsp; [\_read\_file\_object](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.parser/content/functions.md#_read_file_object) &nbsp;&nbsp; [parse](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.parser/content/functions.md#parse) &nbsp;&nbsp; [read](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.parser/content/functions.md#read)
>
> **Constants:** &nbsp; None

# Class Parser
No description.

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|feedable|getter|Isn't anymore feedable when the `[[END]]` tag is encountered||
|sections|getter|None||
|value_converter|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [feed](#feed) &nbsp;&nbsp; [\_strip\_section\_spacing](#_strip_section_spacing) &nbsp;&nbsp; [\_update](#_update)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self, value\_converter=None)





**Return Value:** None

[Back to Top](#module-overview)


## feed
No description



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_strip\_section\_spacing
No description



**Signature:** (self, body)





**Return Value:** None

[Back to Top](#module-overview)


## \_update
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



