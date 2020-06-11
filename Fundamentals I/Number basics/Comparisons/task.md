## Numbers: comparisons

Numbers in Python can be compared in a familiar way.
All of the following comparisons are expressions whose value is a boolean: `True` or `False`.


Equality works as expected:
```text
>>> 1 == 1
True
>>> 1 == 1.0
True
>>> 0.0125 == 1.25e-2
True
>>> 1 == 2
False
```

And also the order comparisons `<`, `<=`, `>`, and `>=` (meaning "less than", "less than or equal to", "greater than", and "greater than or equal to" respectively):

```text
>>> 1 < 1.0
False
>>> 0.999 < 1
True
>>> 1 <= 2
True
>>> 2 >= 1
True
>>> 2 >= 2.0
True
```


Again, we have to be aware of the limited precision of `float`s (see [this giude <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/tutorial/floatingpoint.html) on an explanation for why this happens):
```text
>>> 0.1 + 0.1 + 0.1 == 0.3
False
>>> 1 - 1e-16 < 1
True
>>> 1 - 1e-17 < 1
False
```
