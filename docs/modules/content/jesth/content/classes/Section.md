Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth**
 
For convenience, this module exposes main classes and functions of the library

> **Classes:** &nbsp; [Document](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Document.md#class-document) &nbsp;&nbsp; [Parser](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Parser.md#class-parser) &nbsp;&nbsp; [Section](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/Section.md#class-section) &nbsp;&nbsp; [ValueConverter](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/classes/ValueConverter.md#class-valueconverter)
>
> **Functions:** &nbsp; [create\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#create_dict) &nbsp;&nbsp; [flatten\_dict](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#flatten_dict) &nbsp;&nbsp; [parse](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#parse) &nbsp;&nbsp; [read](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#read) &nbsp;&nbsp; [render](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#render) &nbsp;&nbsp; [split\_key\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#split_key_value) &nbsp;&nbsp; [write](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth/content/functions.md#write)
>
> **Constants:** &nbsp; None

# Class Section
A section is the main unit of a jesthFile. It's composed of a header and a body

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|body|getter|The body in its base form, i.e., a list of strings !||
|header|getter|None||
|value_converter|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [create\_dict](#create_dict) &nbsp;&nbsp; [to\_dict](#to_dict) &nbsp;&nbsp; [to\_text](#to_text) &nbsp;&nbsp; [update](#update)

## \_\_init\_\_
Init a section



**Signature:** (self, header, body=None, \*, value\_converter=None)

|Parameter|Description|
|---|---|
|header|the header (string) of the section|
|body|the body of the section is a string, a list of strings or a dict. Beware, if the body is a dict, instantiating this class may raise exceptions. For example, if the body contains circular references, an exception will be raised. Use the method ".update" if you want to submit a dict as body|
|value\_converter|instance of ValueConverter to customize value encoding|





**Return Value:** None

[Back to Top](#module-overview)


## create\_dict
Try to build a dict object out of the body of this section.
Raise an exception if an error occurs !
Return `default` if the body has been created but is empty



**Signature:** (self, default=None, \*, strict=True)

|Parameter|Description|
|---|---|
|default|Value to return if the body has been successfully converted into an empty dict. Note that `default` will be updated to contain an empty dict (from ValueConverter.dict_type) if you leave it set to None.|
|strict|set True if you don't want to preserve comments and whitespaces|





**Return Value:** If everything is ok, a dict will be returned or the value of `default`
Exceptions will be raised whenever a problem will arise !

[Back to Top](#module-overview)


## to\_dict
Try to convert the body of this section to a dict.
Return a fallback value if failed to convert



**Signature:** (self, default=None, fallback=None, \*, strict=True)

|Parameter|Description|
|---|---|
|default|Value to return if the body has been successfully converted into a dict but empty. Note that `default` will be updated to contain an empty dict (from ValueConverter.dict_type) if you leave it set to None.|
|fallback|Value to return if the attempt to convert the body into a dict failed|
|strict|set True if you don't want to preserve comments and whitespaces|





**Return Value:** If everything is ok, a dict will be returned.
Else the value of `default` or `fallback` will be returned.

[Back to Top](#module-overview)


## to\_text
        Return the body (list of lines) as a text string.

        [return]
        Return a string built with: `"
".join(self._body)`



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## update
Update the entire body. The new body may be string, list of strings or a dict.
Beware, if the body is a dict, instantiating this class may raise exceptions.
For example, if the body contains circular references, an exception will be raised.



**Signature:** (self, body)





**Return Value:** None

[Back to Top](#module-overview)



