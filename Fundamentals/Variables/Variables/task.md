# Variables

Often when writing a program, you need to keep track of a piece of data that changes over time (e.g. the number of items in a shopping cart), or you want to reuse the same object in multiple places (e.g. the name of a user).
These problems can be solved with the use of a [variable <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/variable_(computer_science)).

In Python, creating a variable is essentially giving a name to an object.
The name of a variable is called its *identifier*.
This act of naming an object is called [*assignment* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/Assignment_(computer_science)).

Once we have defined a variable, every time we use its identifier in an expression, upon evaluation, it will get "substituted" with the object it references.

## Identifiers

Valid [identifiers <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) in Python start with a letter (lowercase or uppercase) or an underscore, and are followed by arbitrarily many alphanumeric characters and underscores. Identifiers are case-sensitive.

```python
# valid identifiers
var
abc123
_var
Var
__hello
a_fancy_name_42

# invalid identifiers
123abc
a+bcd
hell[o]
a name with spaces
``` 



## Assignment statement

The syntax to assign an object to an identifier, i.e. to associate the name of a variable with an object, is the following:
```python
<identifier> = <expression>
```
That is, we write the identifier (i.e. the name) of the variable on the left side, followed by a single equals sign, followed by an expression whose value is the object we want to name. This constitutes an [assignment *statement* <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements) —note that this is a statement and not an expression; it doesn't have a value, and you have to place it on its own line.

```python
my_variable = 42
```

## Modifying a variable

After a variable has been defined, it can be "reassigned" to any other object.

```python
var = "hello"
var = 123
var = [42, 3.14]
```

## Examples

```python
my_variable = 42
```

Now, every time we use `my_variable` in an expression, it gets evaluated to the object assigned to the name "my_variable", which is `42`.

```python
print(my_variable + 1)  # prints 43
```

## Assignment, not a copy!

When we assign an object to a name, the object doesn't get copied to a "container" with the given name, like it is in other programming languages. 
Instead, that name is made to "point" at the object we gave it.
Thus, when we modify that object, the changes will be visible through that variable (i.e. when we use the variable, we will see the updated object). 
