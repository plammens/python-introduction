# Special characters in string literals

What happens if you want to insert a double-quote *within* a double-quoted string? We might be tempted to just write it as-is:
```python
"Ada thought "this is fun!" to herself" 
```
But we use double-quotes to [delimit <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/delimiter) the start and end of the string. Thus, when Python reaches the `"` after `thought `, it thinks the string must be over! So anything that comes after it is not interpreted as part of the string, which leads to errors.

The way around this is to write each double-quote within the string with a backslash before it: `\"`. This doesn't indicate a backslash character followed by a double quote, but rather, it is interpreted as a single double-quote character. The example above would become
```python
"Ada thought \"this is fun!\" to herself"  # correct 
```

The exact same happens with single-quotes within single-quoted strings:
```python
'Hi, I\'m Bernard'  # single-quote
``` 

-----------

If you're only using one type of quote within your string, though, you can enclose the string in the opposite type of quote to avoid this problem:
```python
'Ada thought "this is fun!" to herself'  # valid
"Hi, I'm Bernard"  # valid
```
But if you use both types, you're forced to use the backslash:
```python
"Charlie's car is named \"Bob the Second\""  # mixed
```


## Escape sequences

In this context, the backslash character is known as an [**escape character** <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/escape_character), because when it is encountered in a string, it isn't interpreted litteraly as the character `\ `, but rather it indicates a "special sequence" that, as a whole, encodes a single character. Such a sequence is known as an [**escape sequence** <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/escape_sequence).

### Newline

We've just seen two escape sequences: `\"` and `\'`. These encode, respectively, a double- and a single-quote. Another of the most common escape sequences is that for the [**newline** <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/newline) character. This character encodes a line break. The corresponding escape sequence is `\n`.

Inserting `\n` in a string is equivalent to inserting a line break in a multiline literal. Thus, these two strings are equivalent.
```python
"First line\nSecond line"  # with newline character
"""First line
Second line"""  # with line break in multiline string
``` 
In fact, when you insert a line break in a text editor, the editor writes a newline character.

### Literal backslash

Since the backslash is the escape character, if we want to literally insert `\ ` in a string, we need to use another escape sequence: `\\`. This is interpreted as a single backslash character.
````python
"A backslash: \\"  # string with backslash
````

### More

See [here <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/lexical_analysis.html#index-22) for a full list of escape sequences in Python.


## Task

Use the interactive console to play around with escape sequences in string literals!

