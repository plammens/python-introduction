# Basic control flow: `if` statement

**Python docs:**  [if statement <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement)

The `if` (or `if`-`else`) statement is the basic tool for modifying control flow based on a condition.
It is a *compound* statement:

```python
if <expr>:
    <block1>
else:
    <block2>
```

Here, `<expr>` is an expression, and `<block1>` and `<block2>` are code blocks (one or more lines of code) 
When Python encounters such a statement, it first evaluates `<expr>`. That value is implicitly converted to a boolean. If the result is `True`, `<block1>` gets executed. Otherwise, if it is `False`, `<block2>` gets executed.

In other words, an `if`-`else` statement is a compound statement that takes a condition (an expression whose value can be interpreted as `True` or `False`) and two blocks of code.
If the condition is `True` (i.e. the expression evaluates to `True`), the first block gets executed.
Or else (and here's why it's named `else`), the second block gets executed.



