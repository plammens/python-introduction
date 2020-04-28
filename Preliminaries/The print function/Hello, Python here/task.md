# Hello, Python here
**Related official docs**: [The `print` function <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/library/functions.html#print)

Often, when you're writing a program, you want it to produce some kind of output when you run it;
maybe it's the result of a computation, or a status message that indicates what's going on, or
something else.

In Python, the most useful tool for this purpose is the `print` function. The `print` function lets
you write text output to the terminal, and thus is one of the principal ways your program can
communicate with the outside world.

**Note:**
When we use the verb "print" in a Python context (and in many other programming languages), we
usually mean outputting some text to the terminal—do not confuse it with actually printing stuff
on paper using a physical printer!

## How to print?

Whenever you want to output some text to the terminal, you *call* (i.e. execute) the print 
function as follows:
```text
print(<something>)
``` 
Here `<something>` stands for whatever you want to print.

Here's an example of how you would print the text `Hello, world!` to the terminal:
```python
print("Hello, world!")
```

`print` can print any *object* (more on objects later; for now think of an object as any piece of
data), but since its output is always in text form, it first converts the object to be printed to
text (it prints a text representation of the object).

Thus, this also works:
```python
print(42)
```

## Don't forget to print!

Remember how we said that the interactive console always prints the value of expressions you
give as input? Well, that's not the case in general when running a Python program! In fact,
Python won't output anything if you don't explicitly tell it to. So, if you want to see the
result of some expression, just writing the expression on a line in the Python file won't
be enough, you'll have to write that inside a `print` call!

```python
"This won't be printed"  # does nothing
print("This will be printed")  # prints
```

## Task

Take a look at the `main.py` file open in the editor. It contains a bunch of print calls.
Run the file with the <kbd>Run</kbd> button below to see what happens! You can also try to run
each print call line-by-line in the interactive console. 

Feel free to play around with the 
code and experiment different things. Pay attention, in particular to the fact that only stuff
 inside `print( )` is output
to the terminal if you run the file (instead of using the interactive console).

