# Clauses

An `if` statement can be thought of as having  "branches": the code block directly under `if` and the code block directly under `else`.

```python
if <expr>:
    <block1>
else:
    <block2>
```

This is a more general pattern in [compound statements <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/compound_stmts.html). Compound statements are made up of one or more *clauses*, each consisting of a *header* and a *suite*.

The *header* is the line of code that indicates the start of a suite and ends with a colon, and the *suite* is the block of code under a header, indented by one level (i.e. 4 spaces).

In the case of the following `if` statement, 
```python
if var == 2:
    print('spam')
    eggs = 5
else:
    print('ham')
    eggs = 0
```
the two clauses are
```python
if var == 2:
    print('spam')
    eggs = 5
```
and
```python
else:
    print('ham')
    eggs = 0
```

Their headers are, respectively, `if var == 2:` and `else:`. The suites, are, respectively,
```python
print('spam')
eggs = 5
```
and
```python
print('ham')
eggs = 0
```
