# Python's data model: objects
**Relevant official docs:** [Data model <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/datamodel.html)  

Programs need to manipulate data. Python represents data in the form of objects.
Everything in Python is an object.

What is an object? Quoted from the [official documentation <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types):
> Objects are Python’s abstraction for data. All data in a Python program is represented by
> objects or by relations between objects. Every object has an identity, a type and a value.
>
> An object’s identity never changes once it has been created.
>
> An object’s type determines the operations that the object supports (e.g., “does it have a
> length?”) and also defines the possible values for objects of that type.
>
> The value of some objects can change.

As an example, suppose you want to think of a specific car as an object. Its **type** would be
the abstract concept of "car", which defines what cars are like and what attributes they have, e.g.
colour, number of seats, make, model, etc. Its **value** would be comprised of all of the values of
its attributes: e.g. colour='red', number of seats=5, make=Volkswagen, model=Polo, etc.
Finally, its **identity** would be the individual, unique exemplar. While there could be other cars
with the same value (i.e. of the same model, colour, etc.), they would be separate instances, so
their identities would be different.

The value of this car could change, for example, if it gets repainted in another colour.


## Value

The value of an object is the information that it "contains"; it is made up of the attributes of
the object. In our example, "color=red" would be part of the car's value.

### Comparing the value of objects

The value of two objects can be compared with the equality comparison (`==`):
```python
a == b  # "is a equal to b?"
```
Note the double equals sign—not to be confused with variable assignment, which is one equals sign!
To check the opposite, i.e. whether two objects are *not* equal in value, we use `!=`:
```python
a != b  # "is a different to b?"
```

## Identity

The identity of an object is an abstract concept that makes us able to distinguish distinct
objects. Each individual object has a different identity (even if their value is 
equal to that of some other object). 

### Comparing the identity of objects

We can check whether two objects have equal or different identities (i.e. whether they're exact
same instance) with the `is` and `is not` operators respectively:
```python
a is b  # "are a and b the same object?"
a is not b  # "are a and b different objects?"
```

## Type

The type of an object is a "blueprint" that defines the attributes of objects of this kind
and the operations you can perform on them.

You can get the type of an object by using the [`type` function <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/functions.html#type):
```python
type(<object>)
```
where `<object>` is an expression for any object. This is an expression that returns the *type object* of the given object `o`; that is, an object which represents the type of `o`. (We'll see examples of type objects soon.) 

### Checking whether an object is of a certain type

To check whether an object `o` has type `t`, you can use the [isinstance <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/functions.html#isinstance) function:
```python
isinstance(o, t)
```
This expression returns either `True` or `False` (a boolean; more on booleans later).

Note that although using
```python
type(o) is t
```
to check whether `o` is of type `t` would work in some cases, in some other cases it would return `False` when we wouldn't want it to, for reasons we'll see later in the course. Thus for this purpose it's best to always use `isinstance`.


## Task

Look at the file in the editor. It showcases comparisons of value and identity, as well
as usage of the `type` function.


