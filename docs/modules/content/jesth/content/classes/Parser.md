Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth**
 
For convenience, this module exposes main classes and functions of the library

> **Classes:** &nbsp; [Document](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Document.md#class-document) &nbsp;&nbsp; [Parser](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Parser.md#class-parser) &nbsp;&nbsp; [Section](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Section.md#class-section) &nbsp;&nbsp; [ValueConverter](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/ValueConverter.md#class-valueconverter)
>
> **Functions:** &nbsp; [flatten\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#flatten_dict) &nbsp;&nbsp; [make\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#make_dict) &nbsp;&nbsp; [parse](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#parse) &nbsp;&nbsp; [read](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#read) &nbsp;&nbsp; [render](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#render) &nbsp;&nbsp; [split\_key\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#split_key_value) &nbsp;&nbsp; [write](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#write)
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



