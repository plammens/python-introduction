# Numbers: special `float` values

Besides decimal numbers, the float type has a few special values that don't represent "proper" numbers.
 * **Positive infinity**: `float('+inf')` or `float('inf')`. This value is larger than all "normal" `float`s (and `int`s).
 * **Negative infinity**: `float('-inf')`. This value is smaller than all "normal" `float`s (and `int`s).
 * Not a Number (**NaN**): `float('nan')`. A special value to encode the result of a mathematically invalid operation, missing data, or some other numerical error. Similar to `None`, but has type `float` and can be compared with other `float`s. Unlike most objects, NaN is not equal to anything, not even to itself:
    ```text
    >>> float('nan') == float('nan')
    False
    ```


## Value range

The range of values for `float`s is finite and depends on how they're represented in your hardware.

Most machines use the "double precision" format defined in the [IEEE-754 standard <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/IEEE_754), which provides
53 bits of precision for the mantissa and 11 bits for the exponent, meaning the [absolute value <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/absolute_value) of floats is
limited to a range between about `0b0.000...01 * -2**-1022` and `0b1.111...11 * 2**1023` (besides `0.0`, of course).

Precisely, the lower and upper bounds for absolute value (excluding `0.0`) are the following:
```python
# smallest absolute value
float.fromhex('0x0.0000000000001p-1022')
# largest absolute value
float.fromhex('0x1.fffffffffffffp+1023')
```

