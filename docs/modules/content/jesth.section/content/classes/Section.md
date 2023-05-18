Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.section**
 
Definition of the Section class

> **Classes:** &nbsp; [Section](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.section/content/classes/Section.md#class-section)
>
> **Functions:** &nbsp; [ensure\_body](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.section/content/functions.md#ensure_body)
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
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [get\_dict](#get_dict) &nbsp;&nbsp; [make\_dict](#make_dict) &nbsp;&nbsp; [update](#update)

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


## get\_dict
Try to convert the body of this section into a dict.
Return fallback if failed to convert



**Signature:** (self, default=None, fallback=None, \*, strict=True)

|Parameter|Description|
|---|---|
|default|Value to return if the body has been successfully converted into an empty dict. Note that `default` will be updated to contain an empty OrderedDict if you leave it set to None.|
|fallback|Value to return if the attempt to convert the body into a dict failed|
|strict|set True if you don't want to preserve comments and whitespaces|





**Return Value:** If everything is ok, a dict (OrderedDict) will be returned.
Else the value of `default` or `fallback` will be returned.

[Back to Top](#module-overview)


## make\_dict
Try to convert the body of this section into a dict (OrderedDict).
Raise an exception if an error occurs !
Return `default` if the body has been created but is empty



**Signature:** (self, default=None, \*, strict=True)

|Parameter|Description|
|---|---|
|default|Value to return if the body has been successfully converted into an empty dict. Note that `default` will be updated to contain an empty OrderedDict if you leave it set to None.|
|strict|set True if you don't want to preserve comments and whitespaces|





**Return Value:** If everything is ok, a dict (OrderedDict) will be returned or the value of `default`
Exceptions will be raised whenever a problem will arise !

[Back to Top](#module-overview)


## update
Update the entire body. The new body may be string, list of strings or a dict.
Beware, if the body is a dict, instantiating this class may raise exceptions.
For example, if the body contains circular references, an exception will be raised.



**Signature:** (self, body)





**Return Value:** None

[Back to Top](#module-overview)



