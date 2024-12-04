Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.misc**
 
Private miscellaneous functions. Only "split_key_value" is public

> **Classes:** &nbsp; [FloatParts](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/classes/FloatParts.md#class-floatparts) &nbsp;&nbsp; [WriteToFile](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/classes/WriteToFile.md#class-writetofile)
>
> **Functions:** &nbsp; [\_parse\_mantissa](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#_parse_mantissa) &nbsp;&nbsp; [\_prepare\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#_prepare_float) &nbsp;&nbsp; [\_tidy\_up\_right\_mantissa](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#_tidy_up_right_mantissa) &nbsp;&nbsp; [add\_leading\_backslashes](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#add_leading_backslashes) &nbsp;&nbsp; [clean\_leading\_backslashes](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#clean_leading_backslashes) &nbsp;&nbsp; [correct\_index](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#correct_index) &nbsp;&nbsp; [count\_indents](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#count_indents) &nbsp;&nbsp; [decode\_unicode](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#decode_unicode) &nbsp;&nbsp; [encode\_unicode](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#encode_unicode) &nbsp;&nbsp; [ensure\_parent\_dir](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#ensure_parent_dir) &nbsp;&nbsp; [get\_headers](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#get_headers) &nbsp;&nbsp; [parse\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#parse_float) &nbsp;&nbsp; [split\_key\_value](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#split_key_value) &nbsp;&nbsp; [tidy\_up\_bin](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#tidy_up_bin) &nbsp;&nbsp; [tidy\_up\_float](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#tidy_up_float) &nbsp;&nbsp; [tidy\_up\_hex](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#tidy_up_hex) &nbsp;&nbsp; [tidy\_up\_int](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#tidy_up_int) &nbsp;&nbsp; [tidy\_up\_oct](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#tidy_up_oct) &nbsp;&nbsp; [write\_to\_file](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.misc/content/functions.md#write_to_file)
>
> **Constants:** &nbsp; None

# Class FloatParts
FloatParts(left_mantissa, right_mantissa, exponent)

## Base Classes
tuple

## Class Attributes
\_field\_defaults &nbsp;&nbsp; \_fields &nbsp;&nbsp; \_fields\_defaults &nbsp;&nbsp; \_make &nbsp;&nbsp; exponent &nbsp;&nbsp; left\_mantissa &nbsp;&nbsp; right\_mantissa

## Class Properties


# All Methods
[count](#count) &nbsp;&nbsp; [index](#index) &nbsp;&nbsp; [\_asdict](#_asdict) &nbsp;&nbsp; [\_replace](#_replace)

## count
Return number of occurrences of value.

**Inherited from:** tuple

**Signature:** (self, value, /)





**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** tuple

**Signature:** (self, value, start=0, stop=9223372036854775807, /)





**Return Value:** None

[Back to Top](#module-overview)


## \_asdict
Return a new dict which maps field names to their values.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_replace
Return a new FloatParts object replacing specified fields with new values



**Signature:** (self, /, \*\*kwds)





**Return Value:** None

[Back to Top](#module-overview)



