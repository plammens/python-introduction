# Conversion to booleans

## Explicit conversion

**Python docs:** [bool() <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/functions.html#bool)

Any object can be converted to a `bool` by using the `bool` function.
```python
bool(<object>)
```

### Truth value testing

**Python docs:** [truth value testing <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)


Applying the `bool` function to a boolean returns the same boolean.
Any other object is converted to `True`, with the exception of the following (which are converted to `False`):
* constants defined to be "false": `None`
* zero of any numeric type, e.g. `0` or `0.0`
* empty sequences (e.g. strings) and collections (e.g. sets) , e.g. `''`, `()`, `[]`, `{}`, `set()`

```text
>>> bool(True)
True
>>> bool(False)
False
>>> bool("hello")
True
>>> bool([])
False
>>> bool(None)
False
```

This defines an intuitive notion of "truthiness": "empty" or "null" objects (as intuitive concepts) are converted to `False`, and all other objects are converted to `True`.  

## Implicit conversion

**Python docs:** [truth value testing <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), [boolean operations (language reference) <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/expressions.html#boolean-operations)

In Python, objects can be *contextually converted* to booleans. That means that in certain contexts, objects are automatically interpreted as booleans (without explicitly using the `bool` function), using the rules laid out above.

In particular, objects that appear in boolean operations are implicitly converted to booleans.
This allows you to write, for instance `not obj` or `obj1 and obj2` where `obj`, `obj1`, and `obj2` are arbitrary objects.

```text
>>> not None
True
>>> not 3.14
False
```

If you read the fine print in the article about boolean operations, you will have read that the precise definition of `or` and `and` is, respectively, that `x or y` returns `x` if `x` is true and `y` otherwise, and that `x and y` returns `y` if `x` is true and `y` otherwise.
Now that we have seen that `x` and `y` can be any objects, and that their truth value is interpreted following the rules above, you'll understand the following:

```text
>>> [] or [1, 2, 3]
[1, 2, 3]
>>> 0 and True
0
>>> "hello" and ''
''
```

In the first example, `[] or [1, 2, 3]`, the first operand is `[]`, an empty list, which, by the rules mentioned earlier, is considered as false (since it is an empty sequence). Since `x or y` returns `x` if `x` is true and `y` otherwise, the second operand of the `or` operation is returned, which is `[1, 2, 3]`.


## Task

Assign to the variables `a` through `f` the result of the boolean operation specified in the comment (just by thinking!).
