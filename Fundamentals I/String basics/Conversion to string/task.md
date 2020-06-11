# Strings: converting to a string

Every object has a string representation—that's what gets printed when we use `print` on something
which isn't a string.


You can explicitly convert objects to strings using the `str` type.
Calling `str` on an object will return its string representation.
```text
str(<object>)
```
For example:
```text
>>> str(object())
'<object object at 0x0000020819C7EFD0>'
>>> str(0.00001)
'1e-05'
>>> str('hello')
'hello'
>>> str({1, 2, 3})
'{1, 2, 3}'
```


## Task

Look at `task.py`.
You want to print that `2 + 0.00001 == 2.00001` *as text*. Currently though, this is written as-is in the `print` call, which causes Python to evaluate the comparison and return `True`, which is what gets printed!

Use `str` on the numbers along with string concatenation with '+' to print the comparison as text (and not its value, i.e. `True`).
