# String literals

**Relevant docs:** [`str` literals <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)

String values can be directly written in code by the use of a [literal <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/Literal_(computer_programming)) (a "literal" value written in the code).


In Python, string literals are written by enclosing a sequence of characters in either single- or double-quotes:
```python
"hello world"  # a string literal
'hello world'  # exact same thing
```
It doesn't matter what type of quote you use to write your string; they're equivalent.

Unlike other languages, there's no special type for single characters;
they're just one-character strings:
```python
'a'  # still a string
```


## Multiline literals

Strings enclosed with one quotation mark on either side are limited to occupy a single line of code.
```python
"hello world"  # OK

# invalid:
"hello
world"
```

To write strings that span multiple lines, we can use the triple quote syntax (enclosing a sequence of characters, including any line breaks, in three quotation marks):
```python
"""First line.
Second line
Third line"""  # a multiline string
```
This constitutes a multiline string literal.

As before, we can also use single quotes:
```python
'''First line.
Second line
Third line'''  # a multiline string
```

The line breaks in multiline literals are reflected in the string object that is created; that is, if you use any line breaks in your multiline literal, these will be part of the string itself. E.g., if you print 
```python
print("""First line
Second line""")
```
the output will be in two lines:
```text
First line
Second line
```

## Task

The file in the editor contains some string literals for you to play around with in the interactive console.
