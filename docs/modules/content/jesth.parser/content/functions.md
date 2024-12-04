Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.parser**
 
This module exposes read and parse functions that return a document instance

> **Classes:** &nbsp; [Parser](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.parser/content/classes/Parser.md#class-parser)
>
> **Functions:** &nbsp; [\_read\_file\_object](#_read_file_object) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read)
>
> **Constants:** &nbsp; None

# All Functions
[\_read\_file\_object](#_read_file_object) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read)

## \_read\_file\_object
No description



**Signature:** (file, parser)





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


