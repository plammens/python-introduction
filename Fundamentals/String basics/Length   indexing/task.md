# Strings: length & indexing

**Python docs:** [sequences <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/datamodel.html#index-14)

## Length

**Python docs:** [len <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/functions.html#len)

Strings have a length, which corresponds to the number of characters they contain.
We use the `len` function to get the length of a string:
```python
len("abcdef")
```
The resulting value is an `int`.

```text
>>> len("abcdef")
6
```

## Indexing

We can get the *i*-th character of a string (counting from 0) using subscript notation: we write the index enclosed in square brackets to the right of the string we're indexing.
```python
"hello"[0]  # returns 'h'
```
The resulting value is a string of length 1.

```text
>>> "hello"[1]
'e'
```

Since in Python strings are [zero-indexed <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/zero_indexed) (meaning we start counting from 0), the range of valid indexes for a string `s` is `0`, `1`, `2`, ..., up to `len(s) - 1`.

Using an index outside of this range will produce an error:

```text
>>> 'hello'[5]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: string index out of range
```

