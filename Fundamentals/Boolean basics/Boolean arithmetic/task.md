# Boolean arithmetic

**Python docs:** [boolean operations <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not), [boolean operations (language reference) <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/expressions.html#boolean-operations) 

There are three main operations we can perform with booleans in Python: `not`, `and`, and `or`.

The `not` operation is a [*unary operation* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/unary_operation), meanning that it acts on a single boolean—in the same way that a negative sign acts on a single number, returning the negative of a number ($-7$ is negative $7$). 

Both `and` and `or` are [*binary operations* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/binary_operation), meaning that they act on two booleans—one on each "side" of the operator, like addition or multiplication.


All of these operations return another boolean. (This isn't completely accurate, but for now it's useful to think like this.)


## Not

A unary operation that [negates <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/negation), i.e. "inverts", the value of a boolean: if the input is `False`, it returns `True`, and if the input is `True`, it returns `False`.

To write a `not` operation in Python, you write the `not` [*operator* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/operator_(computer_programming)) before the boolean you want to negate.

```python
not False  # returns True
not True   # returns False
```

## And

A binary operation that returns `True` if and only if both input values are `True` (otherwise it returns `False`).

To write an `and` operation in Python, write the `and` operator between the two booleans you want to operate on.

```python
False and False  # returns False
False and True   # returns False
True and False   # returns False
True and True    # returns True
```

(To be precise, `x and y` is an operation that returns `x` if `x` is false and `y` otherwise, which might not be a boolean—more on this soon.)


## Or

A binary operation that returns `True` if and only if either input value is `True` (otherwise it returns `False`).

To write an `or` operation in Python, write the `or` operator between the two booleans you want to operate on.

```python
False or False  # returns False
False or True   # returns True
True or False   # returns True
True or True    # returns True
```

(To be precise, `x or y` is an operation that returns `x` if `x` is true and `y` otherwise, which might not be a boolean—more on this soon.)

