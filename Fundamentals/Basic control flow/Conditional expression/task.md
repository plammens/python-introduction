# Basic control flow: the conditional expression

**Python docs:** [conditional expression <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

Often, you want an expression to have a value if some condition is met an some other value otherwise.

You can do that using an `if`-`else` statement and a variable:
```python
if <condition>:
    value = <expr1>
else:
    value = <expr2>
```
After this, value contains the desired value. This is kind of cumbersome though, since you need to use a new variable and a whole `if` statement when ideally you would want a single expression.

For this purpose, Python has conditional expressions:
```python
<expr1> if <condition> else <expr2>
```
If `<condition>` is true, this expression evaluates `<expr1>` and returns its value; otherwise, `<expr2>`.

This is an expression, so it can be used anywhere where a value can be used:
```python
num = 42
negative = True
print((-1 if negative else 1)*num)
```


## Chaining conditional expressions

Since conditional expressions are expressions, you can nest one within the other. That is, if we have the following,
```python
<expr1> if <condition> else <expr2>
```
`<expr2>` can be another conditional expression:
```python
<expr1> if <condition1> else (<exprA> if <condition2> else <exprB>)
```

Since conditional expressions have the lowest priority of all Python operators, we can safely remove the paretheses:
```python
<expr1> if <condition1> else <expr2> if <condition2> else <expr3>
```
This will return the value of `<expr1>` if `<condition1>` is true, otherwise the value of `<expr2>` if `<condition2>` is true, otherwise `<expression3>`. Thus it is analogous to

```python
if <condition1>:
    value = <expr1>
elif <condition2>:
    value = <expr2>
else:
    value = <expr3>

value
```

Indeed, we can chain arbitrarily many conditionals in this fashion, forming a single expression:
```python
<e1> if <c1> else <e2> if <c2> else ... <eN-1> if <cN-1> else <eN>
```
where `N` is the number of alternative values for this expression.
Analogous to:
```python
if <c1>:
    value = <e1>
elif <c2>:
    value = <c2>
...
elif <cN-1>:
    value = <eN-1>
else:
    value = <eN>

value
```

