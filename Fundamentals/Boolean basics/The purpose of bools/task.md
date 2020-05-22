# Booleans: where are they used?

You might be wondering where we might use booleans in Python code. And if we can only write `True` or `False`, we can certainly compute the result of any boolean operation ourselves beforehand and put that directly into our code, right?

```python
True and (not False or (True and False) and not False)  # why write this
True  # if we can write this?
```


The key insight is that booleans are rarely used directly in code, i.e. writing a literal (one of `True` or `False`). Instead, they usually come up as the result of another operation; most notably, comparisons.

For example, suppose `num` is an integer. How could you check whether `num` is either equal to `1` or greater than `2`? You can make each comparison separately,
```python
num == 1
num > 2
```
but how do you combine them into one?

The answer is boolean operations. When evaluated, the result of each individual comparison is a boolean, i.e. either `True` or `False`. Thus we could get the answer to this specific question in one expression as
```python
(num == 1) or (num > 2)
```

Since boolean operators like `or` have the lowest priority amongst all operators, we can even remove the parentheses:
```python
num == 1 or num > 2
```

Thus comparisons, or more generally, propositions can be combined arbitrarily with boolean operations.

```python
obj is None or isinstance(obj, tuple) and len(obj) == 3 and obj[1] == 42
```

## Chained comparisons

As a shortcut, Python allows us to write chained comparisons:
```python
1 <= 2 <= 3 <= 4
```
This is equivalent to 
```python
1 <= 2 and 2 <= 3 and 3 <= 4
```
That is, chained comparisons are equivalent to writing "consecutive" comparisons one at a time and combinind them with the `and` boolean operator.

Chained comparisons don't have to be in "increasing" or "decreasing" order:
```python
1 < 3 > 2
# equivalent to
1 < 3 and 3 > 2 
```


## Task

Somewhere where you cannot see two objects have been defined: `obj`, an arbitrary object, and `num`, a number. Using boolean operations, save the following booleans:

1. In `boolean1`, save the answer to "is `obj` either a list or a string that starts with `x`?" 
2. In `boolean2`, save the truth value of the proposition "`num` is either a `float` in the range 0.0 to 1.0 (inclusive) or an `int` in the range 0 to 100 (inclusive)" (use comparisons for this one)
3. In `boolean3`, save the truth value of the proposition "`obj` is not a list"
4. In `boolean4`, save the answer to "is `num` smaller than positive infinity?"

As an extra exercise, print out the value of all four booleans. What can you find out about `obj` and `num` from the results you got?
