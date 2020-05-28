# Basic control flow: the `pass` statement

In some cases you want nothing to happen when a piece of code is run.
This is what the `pass` statement is for. This is a simple statement that basically tells Python: "do nothing".
```python
pass  # nothing happens
```

This might seem as highly useless, but there are some cases where it is indeed useful.
In fact, `pass` is not useful in itself, but rather in combination with compound statements.
Since Python requires that any suite in a compound statement is non-empty, you can use `pass` in cases where you want to write a clause in a compound statement with an "empty" suite (a suite which doesn't do anything when run).

For example:
```python
if boolean:
    do_something():
else:
    pass
``` 
If `boolean` is `True`, `do_something()` will run; otherwise nothin will happen. (This first example is not a good one, since as we'll see in the next article there's a shorthand for this, but just to illustrate.)


Some other examples which we'll see later in the course:

```python
try:
    do_something()
except SomeException:
    pass
```

-------------
```python
class CustomException(Exception):
    pass
```
-----------
```python
def foo():
    pass
```
