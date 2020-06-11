# Built-in types
**Relevant official docs:** [Built-in types <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/stdtypes.html)


In the previous lesson whe talked about objects, which have a value, and identity and a type.

In the following pages we will see an overview of the main built-in types. Objects of these types
are used in almost every Python program since they're the basic building blocks for more complex
objects.

We will look at:
 - Strings (`str`)
 - Numeric types
    - Integers (`int`)
    - Floats (`float`)
 - Sequence types
    - Lists (`list`)
    - Tuples (`tuple`)
 - Sets (`set`)
 - Dictionaries (`dict`)
 
 ## Type objects
 
 Each type has an object in Python that represents it. That is, types are objects themselves!
 In the list above, besides the English name of each type, we've written also their "official"
 Python name; that is, the name of the corresponding type object. Try entering,
 for example, `int` (the type object for integers) in the interactive console.
 
 Also: the type of a type object... is the type `type`! Try it: enter `type(type)` in the 
 console.

