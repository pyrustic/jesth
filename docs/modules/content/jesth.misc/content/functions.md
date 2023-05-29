Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.misc**
 
Private miscellaneous functions. Only "split_key_value" is public

> **Classes:** &nbsp; [FloatParts](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/classes/FloatParts.md#class-floatparts)
>
> **Functions:** &nbsp; [\_parse\_mantissa](#_parse_mantissa) &nbsp;&nbsp; [\_prepare\_float](#_prepare_float) &nbsp;&nbsp; [\_tidy\_up\_right\_mantissa](#_tidy_up_right_mantissa) &nbsp;&nbsp; [add\_leading\_backslashes](#add_leading_backslashes) &nbsp;&nbsp; [clean\_leading\_backslashes](#clean_leading_backslashes) &nbsp;&nbsp; [correct\_index](#correct_index) &nbsp;&nbsp; [count\_indents](#count_indents) &nbsp;&nbsp; [decode\_unicode](#decode_unicode) &nbsp;&nbsp; [encode\_unicode](#encode_unicode) &nbsp;&nbsp; [ensure\_parent\_dir](#ensure_parent_dir) &nbsp;&nbsp; [get\_headers](#get_headers) &nbsp;&nbsp; [parse\_float](#parse_float) &nbsp;&nbsp; [split\_key\_value](#split_key_value) &nbsp;&nbsp; [tidy\_up\_bin](#tidy_up_bin) &nbsp;&nbsp; [tidy\_up\_float](#tidy_up_float) &nbsp;&nbsp; [tidy\_up\_hex](#tidy_up_hex) &nbsp;&nbsp; [tidy\_up\_int](#tidy_up_int) &nbsp;&nbsp; [tidy\_up\_oct](#tidy_up_oct) &nbsp;&nbsp; [update\_cached\_refs](#update_cached_refs)
>
> **Constants:** &nbsp; None

# All Functions
[\_parse\_mantissa](#_parse_mantissa) &nbsp;&nbsp; [\_prepare\_float](#_prepare_float) &nbsp;&nbsp; [\_tidy\_up\_right\_mantissa](#_tidy_up_right_mantissa) &nbsp;&nbsp; [add\_leading\_backslashes](#add_leading_backslashes) &nbsp;&nbsp; [clean\_leading\_backslashes](#clean_leading_backslashes) &nbsp;&nbsp; [correct\_index](#correct_index) &nbsp;&nbsp; [count\_indents](#count_indents) &nbsp;&nbsp; [decode\_unicode](#decode_unicode) &nbsp;&nbsp; [encode\_unicode](#encode_unicode) &nbsp;&nbsp; [ensure\_parent\_dir](#ensure_parent_dir) &nbsp;&nbsp; [get\_headers](#get_headers) &nbsp;&nbsp; [parse\_float](#parse_float) &nbsp;&nbsp; [split\_key\_value](#split_key_value) &nbsp;&nbsp; [tidy\_up\_bin](#tidy_up_bin) &nbsp;&nbsp; [tidy\_up\_float](#tidy_up_float) &nbsp;&nbsp; [tidy\_up\_hex](#tidy_up_hex) &nbsp;&nbsp; [tidy\_up\_int](#tidy_up_int) &nbsp;&nbsp; [tidy\_up\_oct](#tidy_up_oct) &nbsp;&nbsp; [update\_cached\_refs](#update_cached_refs)

## \_parse\_mantissa
No description



**Signature:** (s)





**Return Value:** None

[Back to Top](#module-overview)


## \_prepare\_float
No description



**Signature:** (s)





**Return Value:** None

[Back to Top](#module-overview)


## \_tidy\_up\_right\_mantissa
No description



**Signature:** (s, width)





**Return Value:** None

[Back to Top](#module-overview)


## add\_leading\_backslashes
Add one leading backslash only when the immediately-or-lately first non-backlash
character on the line is an opening square bracket.



**Signature:** (line)





**Return Value:** None

[Back to Top](#module-overview)


## clean\_leading\_backslashes
Remove one leading backslash only when the immediately-or-lately first non-backlash
character on the line is an opening square bracket.



**Signature:** (line)





**Return Value:** None

[Back to Top](#module-overview)


## correct\_index
Correct an index given to access an item in a list



**Signature:** (index, size, ignore\_upper\_bound=False)





**Return Value:** Return a corrected index integer

[Back to Top](#module-overview)


## count\_indents
No description



**Signature:** (line)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_unicode
Take in input some string that might have Unicode escape sequences.
Output the same string with unicode escape sequences converted into
the actual characters that they represent



**Signature:** (text)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_unicode
Convert a string into another where non-latin characters are
replaced with Unicode escape sequences



**Signature:** (text, codec='latin-1')





**Return Value:** None

[Back to Top](#module-overview)


## ensure\_parent\_dir
Make sure that parent dir exists (create it if isn't yet created)



**Signature:** (path)





**Return Value:** None

[Back to Top](#module-overview)


## get\_headers
returns the set of headers from this list of sections



**Signature:** (sections)





**Return Value:** None

[Back to Top](#module-overview)


## parse\_float
Parse a float number (string or decimal.Decimal or float), returns
an instance of this namedtuple:
FloatParts = namedtuple('FloatParts', ['left_mantissa', 'right_mantissa', 'exponent'])



**Signature:** (s)





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
|error.Error|if the separator, the key, or the value is missing,|



**Return Value:** Returns a ("key", "value") tuple if everything is Ok

[Back to Top](#module-overview)


## tidy\_up\_bin
Tidy up some bin int number (str or int)
Example: 0b10011101011 -> 0b100_1110_1011



**Signature:** (s, width=4)





**Return Value:** None

[Back to Top](#module-overview)


## tidy\_up\_float
Tidy up a float number (str or float or decimal.Decimal)
Example: 3.141234 -> 3.141_234



**Signature:** (s, width=3)





**Return Value:** None

[Back to Top](#module-overview)


## tidy\_up\_hex
Tidy up some hex int number (str or int)
Example: 0xA3001F12A34 -> 0xA30_01F1_2A34



**Signature:** (s, width=4)





**Return Value:** None

[Back to Top](#module-overview)


## tidy\_up\_int
Tidy up some int number (str or int)
Example: 300141234 -> 300_141_234



**Signature:** (s, width=3)





**Return Value:** None

[Back to Top](#module-overview)


## tidy\_up\_oct
Tidy up some oct int number (str or int)
Example: 0o45631456202 -> 0o456_3145_6202



**Signature:** (s, width=4)





**Return Value:** None

[Back to Top](#module-overview)


## update\_cached\_refs
No description



**Signature:** (value, cached\_refs)





**Return Value:** None

[Back to Top](#module-overview)


