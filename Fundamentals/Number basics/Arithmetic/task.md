# Numbers: arithmetic

**Python docs:** [binary arithmetic operators <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)

One can perform arithmetic operations with numbers in Python using arithmetic operators such as `+`. All of these operations are expressions whose value is another number.

All of the familiar arithmetic operations are supported in Python:

  * **addition**: $a + b$ in Python is expressed as `a + b`.
    ```python
    12.2 + 13 
    ```
  * **subtraction**: $a - b$ in Python is expressed as `a - b`.
    ```python
    18 - 15
    ```
  * **multiplication**: $a\cdot b$ in Python is expressed as `a * b`
    ```python
    2 * 3.5
    ```
  * (exact) **division**: $\frac{a}{b}$ in Python is expressed as `a/b`
    ```python
    7/3
    ```

Additionally, "negating" a number (i.e. getting its negative) is considered as a [unary operation <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/unary_operation):
```python
-1
--1  # equivalent to -(-1) i.e. 1
```
This operation is known as **negation**.

There are some more arithmetic operations:

  * **integer division**: $\left\lfloor \frac{a}{b} \right\rfloor$ (this is equivalent to the result of exact division truncated down to the nearest integer; i.e. with the [*floor function* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/floor_function) applied to it, or the largest integer $c$ such that $c\cdot b < a$) expressed in Python as `a//b`
    ```python
    5//-3
    ```
  * **modulus**: `a%b` in Python is the modulus operation—the remainder of the integer division `a//b`. That is, it's the number `c` such that `a == (a//b)*b + c`.
    ```python
    7%3
    ```
  * **exponentiation**: $a^b$ in Python is expressed as `a**b`.
    ```python
    13**2
    ```
  
  
## Mixing `int`s and `float`s

Operating two `int`s usually returns an `int`.
Operating two numbers where at least one of them is a `float` usually returns a float:
```text
>>> 1 + 1
2
>>> 1 + 1.0
2.0
>>> 6.0 * 2.0
12.0
```

(With the exception of exact division—`a/b` always returns a `float`, even if the exact result is an integer:
```text
>>> 6/2
3.0
```
)

This is because `float` is the "common type" of `int`s and `float`s: every `int` can be represented as a `float` (but not the other way around).


## The modulo operation

Here we will go a bit more in depth on what the modulo operation does and why it is useful.
Integer division and the modulo operation are related by the following identity (that is, this statement is always true for any numbers `a` and `b` in Python):
```python
a == (a//b)*b + (a%b)
``` 

Taking a concrete example: the division ``7//3``. The number $3$ fits into $7$ two times with a remainder of $1$. This means that `7//3 == 2` and `7%3 == 1`.

This is useful, for instance, to check whether a number is a multiple of another. Checking whether `n` is a multiple of `m` is the same as asking whether the remainder of dividing `n` by `m` is zero; that, is `n % m == 0`. So, to check whether a number `n` is even, we would check whether `n % 2 == 0`.


## Operator precedence

You can combine arbitrarily many operations in an expression:
```python
3 + 13*(7//(5%2) + 10**5) + 3*(4 - 5)/2
```

The priority of operators in expressions combining multiple operations (i.e. which operations get evaluated first) is the conventional one:

0. Parentheses `()`
1. Exponentiation `**`
2. Negation `-`
3. Multiplication `*`, division `/`, integer division `//`, modulus `%`
4. Addition `+`, subtraction `-`


## Task

Assign the result of $1532\cdot 7 - 56$ to the variable `num` (without pre-computing the result). Assign the remainder of dividing that by 13 to the variable `remainder`.
