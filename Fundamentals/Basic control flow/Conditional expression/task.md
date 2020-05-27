# Basic control flow: the conditional expression

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

