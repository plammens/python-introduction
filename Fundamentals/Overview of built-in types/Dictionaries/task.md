# Dictionaries
**Official docs:** [Mapping types <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) 

Dictionaries are mapping from unique *keys* to *values*. That is, they are a collection of
unique objects (*keys*) each of which has another object associated with them (a *value*—not
to be confused with the value of the key itself). Think of a real word dictionary, e.g. an
English dictionary: the keys would be the word entries, and the values would be their 
corresponding definitions.
The type object for dictionaries is `dict`.

You can write a string using a comma-separated list within curly brackets:
```python
{1, "spam", 3}
```

Sets don't contain duplicates, so the following set is equivalent to the one above:
```python
{1, 1, "spam", 3}
```



