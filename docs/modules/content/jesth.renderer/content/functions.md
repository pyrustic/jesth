Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.renderer**
 
This module exposes render and write functions

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [\_write\_to\_file](#_write_to_file) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [write](#write)
>
> **Constants:** &nbsp; None

# All Functions
[\_write\_to\_file](#_write_to_file) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [write](#write)

## \_write\_to\_file
No description



**Signature:** (destination, data)





**Return Value:** None

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


## write
Convert a jesth document into plain text then write it in a file



**Signature:** (document, destination)

|Parameter|Description|
|---|---|
|document|an instance of jesth.document.Document|
|destination|path string, or pathlib.Path instance to a file in which the rendered Jesth text can be saved.|





**Return Value:** Returns the rendered plain text

[Back to Top](#module-overview)


