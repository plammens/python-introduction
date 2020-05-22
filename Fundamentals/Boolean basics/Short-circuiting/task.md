# Booleans: short-circuiting

**Python docs:** [boolean operations <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not), [boolean operations (language reference) <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/expressions.html#boolean-operations) 

Boolean operations in Python are [*short-circuiting* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/Short-circuit_evaluation), meaning that if the result of a binary operation can be determined by evaluating only the first of the two operands, the second operand is not evaluated.

## `and`

Consider the expression `x and y`, where `x` and `y` stand for arbitrary expressions.
Suppose that upon evaluating `x`, we find that `x` is (or is interpreted as) `False`. 
Since an `and` operation is `True` if and only if *both* operands are true, and we know that at least one of them (i.e., `x`) is false, we don't need to find out what `y` is to determine that the whole operation will return `False`.

And that's precisely what Python does: since `x` evaluated to `False`, it skips evaluating `y` and returns `False` directly.

## `or`

Similarly, consider the expression `x or y`, where `x` and `y` stand for arbitrary expressions.
Suppose that upon evaluating `x`, we find that `x` is (or is interpreted as) `True`. 
Since an `or` operation is `True` if *any* of its operands are true, and we know that at least one of them (i.e., `x`) is, we don't need to find out what `y` is to determine that the whole operation will return `True`. 

And that's precisely what Python does: since `x` evaluated to `True`, it skips evaluating `y` and returns `True` directly.


## Implications

This has several implications. For one, short-circuiting allows us to avoid the unnecessary evaluation of the second operand, which might involve expensive (slow) computations:
```python
x or <a very expensive expression to compute>
```
If `x` evaluates to `True`, this will return `True` without making the expensive computations.

But, perhaps more importantly, it allows us to chain boolean operations based on the assumption of the result of a previous operand: when we write `y` in `x and y`, we can safely assume that `x` is true when (or rather, if) `y` gets computed.

Suppose, for example, that you want to check whether an object `obj` is a string that starts with the character `a`. We can do that with an `and` operation:
```python
isinstance(obj, str) and obj[0] == 'a'
```
Suppose `obj` is not a string; suppose for instance it is a number; thus in principle we would expect this operation to return `False`.

If `and` wasn't short-circuiting, both sides of the operation would get computed, regardless of their values. In particular, `obj[0] == 'a'` would get evaluated. But `obj[0]` has no meaning when `obj` is a number—in fact, it raises an error! Thus it would result in an error instead of returning `False`, as intended.

But `and` *is* indeed short-circuiting. Thus, upon computing `isinstance(obj, str)`, since that returns `False` (because `obj` is not a string), Python stops there and returns `False`, *without* evaluating `obj[0] == 'a'` (which would result in an error).

