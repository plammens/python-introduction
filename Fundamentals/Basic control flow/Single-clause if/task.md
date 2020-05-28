## Single-clause `if`

If you want something to run only if a condition is true, and otherwise run nothing, you can omit the `else` clause. 
```python
if <expr>:
    <block1>
```

This is equivalent to
````python
if <expr>:
    <block1>
else:
    pass
````

