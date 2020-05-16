# Numbers: literals

As with strings, we can use number literals to insert a fixed numeric value in Python code.

## Integer literals

**Python docs:** [integer literals <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals)

To write a number in base-10 (i.e. the numbers you see every day), we write a sequence of digits, with an optional negative sign preceding it. 

```python
42
-1
301
```

Note that you can't have any leading zeros in these literals (except for when representing the number `0`).

```python
0123  # wrong
```

You can optionally insert underscores between digits for grouping purposes (to improve readability).

```python
10_000_000
```

You can also write integers in [**b**inary <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/binary), [**o**ctal <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/octal) or [he**x**adecimal <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/hexadecimal) by using the `0b`, `0o` or `0x` prefix respectively. 

```python
# non- base-10:
0b01101001  # binary
0o0151  # octal
0x6f  # hexadecimal
```




## Floating-point literals

**Python docs:** [floating-point literals <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals)

The most basic form of float literal consists of a sequence of digits (the integer part), followed by a decimal dot followed by another sequence of digits (the fractional part).
In this case leading zeros are allowed (though they're not really useful).
You can use underscores to group digits here too.

```python
2.3
08.001
3.14_15_93  # same as 3.141593
```

If the number you're representing as a float happens to be a whole number, you can omit the fractional part.
Similarly, if the number you're representing has integer part equal to zero, you can omit the integer part.

```python
4.  # same as 4.0
.25  # same as 0.25
```

You can also write floats in [E-notation <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/Scientific_notation#E_notation), by writing the mantissa $m$ followed by the character `e` followed by the exponent $n$. This represents the number $m\cdot 10^{n}$. The exponent can be negative

```python
-1e-5  # same as -0.00001
2.35e5  # same as 235_000.0 
```
