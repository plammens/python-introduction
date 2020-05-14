# String concatenation

Two strings can be chained together with the `+` operator:
```python
"hello " + "world"
```
The result is a string that contains all characters from the first string immediately followed
by all characters from the second string:
```text
>>> "hello " +  "world"
'hello world'
```

Since this operation is [*associative* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/Operator_associativity), you can chain arbitrarily many strings with this syntax:
```python
"spam" + "eggs" + "ham"  # concatenation of 3 strings
```


## Task

Look at the file open in your editor, `task.py`.
Your goal is to print
```text
My name is <name> and I'm <age> years old
```
substituting `<name>` with your name and `<age>` with your age.
To do so, you will have to modify the `name` and `age` variables (just modify the strings after `name = ` and `age = ` respectively!) and use string concatenation (with `+`) in the `print` call to "fill in" the values of `name` and `age` in the string. 

Use the variables `name` and `age` directly, don't copy their value in manually!
