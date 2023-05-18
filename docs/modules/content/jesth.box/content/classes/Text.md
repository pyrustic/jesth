Back to [All Modules](https://github.com/pyrustic/jesth/blob/master/docs/modules/README.md#readme)

# Module Overview

**jesth.box**
 
Boxes to hold contents like Jesth Comments, raw texts, or whitespaces...

> **Classes:** &nbsp; [BinInt](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/BinInt.md#class-binint) &nbsp;&nbsp; [Comment](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/Comment.md#class-comment) &nbsp;&nbsp; [CommentID](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/CommentID.md#class-commentid) &nbsp;&nbsp; [HexInt](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/HexInt.md#class-hexint) &nbsp;&nbsp; [N](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/N.md#class-n) &nbsp;&nbsp; [OctInt](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/OctInt.md#class-octint) &nbsp;&nbsp; [RawString](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/RawString.md#class-rawstring) &nbsp;&nbsp; [RawText](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/RawText.md#class-rawtext) &nbsp;&nbsp; [Text](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/Text.md#class-text) &nbsp;&nbsp; [Whitespace](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/Whitespace.md#class-whitespace) &nbsp;&nbsp; [WhitespaceID](https://github.com/pyrustic/jesth/blob/master/docs/modules/content/jesth.box/content/classes/WhitespaceID.md#class-whitespaceid)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Text
Box to hold Text, i.e., multiline string with unicode escape sequences support

## Base Classes
str

## Class Attributes
maketrans (inherited from str)

## Class Properties


# All Methods
[capitalize](#capitalize) &nbsp;&nbsp; [casefold](#casefold) &nbsp;&nbsp; [center](#center) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [expandtabs](#expandtabs) &nbsp;&nbsp; [isalnum](#isalnum) &nbsp;&nbsp; [isalpha](#isalpha) &nbsp;&nbsp; [isascii](#isascii) &nbsp;&nbsp; [isdecimal](#isdecimal) &nbsp;&nbsp; [isdigit](#isdigit) &nbsp;&nbsp; [isidentifier](#isidentifier) &nbsp;&nbsp; [islower](#islower) &nbsp;&nbsp; [isnumeric](#isnumeric) &nbsp;&nbsp; [isprintable](#isprintable) &nbsp;&nbsp; [isspace](#isspace) &nbsp;&nbsp; [istitle](#istitle) &nbsp;&nbsp; [isupper](#isupper) &nbsp;&nbsp; [join](#join) &nbsp;&nbsp; [ljust](#ljust) &nbsp;&nbsp; [lower](#lower) &nbsp;&nbsp; [lstrip](#lstrip) &nbsp;&nbsp; [partition](#partition) &nbsp;&nbsp; [replace](#replace) &nbsp;&nbsp; [rjust](#rjust) &nbsp;&nbsp; [rpartition](#rpartition) &nbsp;&nbsp; [rsplit](#rsplit) &nbsp;&nbsp; [rstrip](#rstrip) &nbsp;&nbsp; [split](#split) &nbsp;&nbsp; [splitlines](#splitlines) &nbsp;&nbsp; [strip](#strip) &nbsp;&nbsp; [swapcase](#swapcase) &nbsp;&nbsp; [title](#title) &nbsp;&nbsp; [translate](#translate) &nbsp;&nbsp; [upper](#upper) &nbsp;&nbsp; [zfill](#zfill)

## capitalize
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower
case.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## casefold
Return a version of the string suitable for caseless comparisons.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## center
Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

**Inherited from:** str

**Signature:** (self, width, fillchar=' ', /)





**Return Value:** None

[Back to Top](#module-overview)


## encode
Encode the string using the codec registered for encoding.

encoding
  The encoding in which to encode the string.
errors
  The error handling scheme to use for encoding errors.
  The default is 'strict' meaning that encoding errors raise a
  UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
  'xmlcharrefreplace' as well as any other name registered with
  codecs.register_error that can handle UnicodeEncodeErrors.

**Inherited from:** str

**Signature:** (self, /, encoding='utf-8', errors='strict')





**Return Value:** None

[Back to Top](#module-overview)


## expandtabs
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

**Inherited from:** str

**Signature:** (self, /, tabsize=8)





**Return Value:** None

[Back to Top](#module-overview)


## isalnum
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and
there is at least one character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isalpha
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there
is at least one character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isascii
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isdecimal
Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isdigit
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there
is at least one character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isidentifier
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
such as "def" or "class".

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## islower
Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and
there is at least one cased character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isnumeric
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at
least one character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isprintable
Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in
repr() or if it is empty.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isspace
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there
is at least one character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## istitle
Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## isupper
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and
there is at least one cased character in the string.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## join
Concatenate any number of strings.

The string whose method is called is inserted in between each given string.
The result is returned as a new string.

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

**Inherited from:** str

**Signature:** (self, iterable, /)





**Return Value:** None

[Back to Top](#module-overview)


## ljust
Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

**Inherited from:** str

**Signature:** (self, width, fillchar=' ', /)





**Return Value:** None

[Back to Top](#module-overview)


## lower
Return a copy of the string converted to lowercase.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## lstrip
Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

**Inherited from:** str

**Signature:** (self, chars=None, /)





**Return Value:** None

[Back to Top](#module-overview)


## partition
Partition the string into three parts using the given separator.

This will search for the separator in the string.  If the separator is found,
returns a 3-tuple containing the part before the separator, the separator
itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string
and two empty strings.

**Inherited from:** str

**Signature:** (self, sep, /)





**Return Value:** None

[Back to Top](#module-overview)


## replace
Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.

**Inherited from:** str

**Signature:** (self, old, new, count=-1, /)





**Return Value:** None

[Back to Top](#module-overview)


## rjust
Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

**Inherited from:** str

**Signature:** (self, width, fillchar=' ', /)





**Return Value:** None

[Back to Top](#module-overview)


## rpartition
Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If
the separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings
and the original string.

**Inherited from:** str

**Signature:** (self, sep, /)





**Return Value:** None

[Back to Top](#module-overview)


## rsplit
Return a list of the words in the string, using sep as the delimiter string.

  sep
    The delimiter according which to split the string.
    None (the default value) means split according to any whitespace,
    and discard empty strings from the result.
  maxsplit
    Maximum number of splits to do.
    -1 (the default value) means no limit.

Splits are done starting at the end of the string and working to the front.

**Inherited from:** str

**Signature:** (self, /, sep=None, maxsplit=-1)





**Return Value:** None

[Back to Top](#module-overview)


## rstrip
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

**Inherited from:** str

**Signature:** (self, chars=None, /)





**Return Value:** None

[Back to Top](#module-overview)


## split
Return a list of the words in the string, using sep as the delimiter string.

sep
  The delimiter according which to split the string.
  None (the default value) means split according to any whitespace,
  and discard empty strings from the result.
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.

**Inherited from:** str

**Signature:** (self, /, sep=None, maxsplit=-1)





**Return Value:** None

[Back to Top](#module-overview)


## splitlines
Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and
true.

**Inherited from:** str

**Signature:** (self, /, keepends=False)





**Return Value:** None

[Back to Top](#module-overview)


## strip
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

**Inherited from:** str

**Signature:** (self, chars=None, /)





**Return Value:** None

[Back to Top](#module-overview)


## swapcase
Convert uppercase characters to lowercase and lowercase characters to uppercase.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## title
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining
cased characters have lower case.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## translate
Replace each character in the string using the given translation table.

  table
    Translation table, which must be a mapping of Unicode ordinals to
    Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for instance a
dictionary or list.  If this operation raises LookupError, the character is
left untouched.  Characters mapped to None are deleted.

**Inherited from:** str

**Signature:** (self, table, /)





**Return Value:** None

[Back to Top](#module-overview)


## upper
Return a copy of the string converted to uppercase.

**Inherited from:** str

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## zfill
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

**Inherited from:** str

**Signature:** (self, width, /)





**Return Value:** None

[Back to Top](#module-overview)



