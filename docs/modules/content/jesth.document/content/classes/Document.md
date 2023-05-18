Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.document**
 
Document class for creating model for Jesth data or to interacting with a Jesthfile

> **Classes:** &nbsp; [Document](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.document/content/classes/Document.md#class-document)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Document
Create a model for Jesth data or for interacting with a JesthFile

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|headers|getter|None||
|path|getter|None||
|path|setter|None||
|sections|getter|None||
|sections|setter|None||
|value_converter|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [append](#append) &nbsp;&nbsp; [count](#count) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [get\_all](#get_all) &nbsp;&nbsp; [insert](#insert) &nbsp;&nbsp; [remove](#remove) &nbsp;&nbsp; [remove\_all](#remove_all) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [save](#save) &nbsp;&nbsp; [save\_to](#save_to) &nbsp;&nbsp; [\_create\_model](#_create_model) &nbsp;&nbsp; [\_insert](#_insert) &nbsp;&nbsp; [\_setup](#_setup) &nbsp;&nbsp; [\_update\_model](#_update_model)

## \_\_init\_\_
Init the document



**Signature:** (self, path=None, sections=None, \*, value\_converter=None)

|Parameter|Description|
|---|---|
|path|if the document is linked to a JesthFile,`path` contains the path to this file. Path might also be a pathlib.Path instance.|
|sections|list of sections (or tuple)|
|value\_converter|an instance of jesth.converter.ValueConverter|





**Return Value:** None

[Back to Top](#module-overview)


## append
Create a new section then append it to the end of this document



**Signature:** (self, header, body=None)

|Parameter|Description|
|---|---|
|header|the header (string) of the new section|
|body|the body of this section as a string or a list of strings|





**Return Value:** None

[Back to Top](#module-overview)


## count
Count the number of sections whose headers match with the
`header` parameter



**Signature:** (self, header)

|Parameter|Description|
|---|---|
|header|the header (string) of the sections|





**Return Value:** Returns the integer number of sections matching with the `header` parameter

[Back to Top](#module-overview)


## get
Get X named section object located at Y index relatively to others sections with same header



**Signature:** (self, header, index=-1)

|Parameter|Description|
|---|---|
|header|the header (string) of the section|
|index|integer index, relatively to the section family (sections sharing this same header). Defaults to -1, thus will be returned, the last section with this header relatively to this header family.|





**Return Value:** Returns a section or None

[Back to Top](#module-overview)


## get\_all
Get all sections sharing same header



**Signature:** (self, header)

|Parameter|Description|
|---|---|
|header|the header (string) of the sections|





**Return Value:** Returns a list of sections whose headers match with the `header` parameter.

[Back to Top](#module-overview)


## insert
Create a new section then insert it in the document at a specific index



**Signature:** (self, index, header, body=None)

|Parameter|Description|
|---|---|
|index|integer index (absolute index). Accepts -1 to mimic the "append" method|
|header|the header (string) of the new section|
|body|the body of this section as a string or a list of strings|





**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove a section from this document



**Signature:** (self, header, index=-1)

|Parameter|Description|
|---|---|
|header|the header of the section to remove|
|index|the index (integer) of the section relatively to its family (sections sharing same header). Defaults to -1, thus the last section of the given header family will be removed from the document|





**Return Value:** None

[Back to Top](#module-overview)


## remove\_all
Remove all sections with this specific header



**Signature:** (self, header)

|Parameter|Description|
|---|---|
|header|the header of the section to remove|





**Return Value:** None

[Back to Top](#module-overview)


## render
Render the entire document or a specific set of sections, i.e.,
returns a Jesth string that may be stored in a file.



**Signature:** (self, \*headers, spacing=1)

|Parameter|Description|
|---|---|
|\*headers|Headers of sections to render. Omitting this will render the entire section|
|spacing|number of empty lines between two adjacent sections. Defaults to 1 empty line.|





**Return Value:** Returns a string that contains sections (each made of square-brackets delimited header
and associated body)

[Back to Top](#module-overview)


## save
Save the recent modifications if this document is linked to a JesthFile,
 i.e., the path parameter has been set.



**Signature:** (self)





**Return Value:** Returns True or False

[Back to Top](#module-overview)


## save\_to
Save the document in a specific filename



**Signature:** (self, path)

|Parameter|Description|
|---|---|
|path|path to filename. Path may be a pathlib.Path instance|





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_model
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_insert
No description



**Signature:** (self, index, header, body)





**Return Value:** None

[Back to Top](#module-overview)


## \_setup
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_model
No description



**Signature:** (self, header, index, section)





**Return Value:** None

[Back to Top](#module-overview)



