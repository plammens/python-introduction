# Python's interactive console
**Related official docs**: 
[Top-level components <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/toplevel_components.html)

Python is an interpreted language, so when we run a Python file the interpreter is executing the
instructions "line-by-line". This has a great advantage: we can use the interpreter to run single
lines or blocks of code, one at a time, so that we can directly interact with the results of
individual computations. This is what the interactive console is all about.


## Starting the interactive console in the command-line

The standard Python interpreter comes with an interactive console that lets you execute code one
 block at a time, i.e. where you can control the execution of code manually.

To run the interactive console in the terminal, run the `python` command without arguments.
Try it now! 
Open the terminal (<kbd>&shortcut:ActivateTerminalToolWindow;</kbd>), type the following and
 press <kbd>Enter</kbd>: 
```bash
python
```
You should see a prompt similar to the following coming up:
```text
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Running some code

In the interactive console, the prompt is indicated by `>>>`. To run code in the interactive console, you must type your line of code after the `>>>` and
press <kbd>Enter</kbd>.

Try running some of the following lines! To illustrate, for the first example, type 
`print("Hello, world!")`) after the `>>>` so that it looks like this:
```text
>>> print("Hello, world!")
```
and press <kbd>Enter</kbd>.

#### Sample lines of code to run:

```python
print("Hello, world!")
```
-------------
```python
8 - 5
```
------------
```python
assert True
```
------------
```python
"spam" + "eggs"
```

### Multiline commands

You can enter a line break in your command by pressing <kbd>Shift+Enter</kbd> (pressing 
<kbd>Enter</kbd> will run it!). This allows you to run multi-line bits of code as one command.
Type the following code in the interactive console as one command:
```python
var = True
if var:
    print('yes')
```


### Quitting the console

To quit the interactive console and return to the terminal prompt, type `quit()`.


## Features of the interactive console

### It replies!

As you might have seen, the interactive console seems to sometimes display some output when you run
a line of code. This is because if you enter an *expression* into the interactive console, its
value will be displayed after it gets computed. We'll go into more details about what
expressions are later, but for now it's enough to know that an expression is any piece of code that
has a value that you can compute: `3.14`, `"hello"`, `1 + 1`, and `round(3.5)` are all expressions.

Here are some examples of expressions. See what happens when you enter them (one-by-one!) in the
interactive console (again, there's no need to understand what's going on in each line yet):

```python
3 + 4*10
```
-------------
```python
round(3.5)
```
------------
```python
"monty python".title()
```

There is one exception, though: if any expression evaluates to (i.e. has value) `None`, the console
doesn't print anything. `None` is a special value that encodes, funnily enough, an absence of 
value. Try typing `None` in the interactive console and press enter, and see what happens. We'll
see why this matters later on.


### It remembers!

Anything you create or modify when entering a command in the interactive console is "remembered"
throughout the whole session (i.e. as long as you keep the console running). This means that the
commands that you enter in the interactive console are not individual "mini-programs", but they're
part of the same program which you write interactively, so to speak.

The following example illustrates this. First, we assign the number 3 to a variable named `var`.
we just enter `var` in the console (which
constitutes an expression) to see the value of var; the console outputs `3`.
Then, we increment the value of `var` by one. Finally we check its value again; the console outputs
 `4`. (More on the details of how variables work later; for now, suffice it to say that they're
named containers for a value.)
```text
>>> var = 3
>>> var
3
>>> var += 1
>>> var
4
```
(Here the `>>>` is the interactive console prompt; what comes after it is the entered command.
Output lines come immediately after their corresponding command, and are *not* prefixed by `>>>`.)



## In PyCharm

In PyCharm, you can directly open an enhanced version of the interactive console by clicking on the
corresponding item in the bottom toolbar: ![console tooltip](static/console-tooltip.png)
Whenever you're working in PyCharm it's best to use this integrated console, since it works well
with other components of the IDE.


### Running a line from a file on the interactive console

PyCharm allows you to run individual lines or a selections of code from a Python file in the
interactive console by pressing <kbd>&shortcut:ExecuteInPyConsoleAction;</kbd>.
This will run the line the caret is on, or the selected text if you have made a selection in the
editor. This feature is very useful if you want to interactively test parts of your program, or
run through your program line by line. 

You can run multiple lines at once by selecting multiple lines of code and then pressing
<kbd>&shortcut:ExecuteInPyConsoleAction;</kbd>.

Try it now! The `main.py` file open in your editor contains some code
for you to try this on. Place the text cursor on the line you want to execute, and press
<kbd>&shortcut:ExecuteInPyConsoleAction;</kbd>.

As a good thinking exercise, try running the whole file using the <kbd>Run</kbd>
button below as well, and compare the difference in output between that and running the
whole file line by line in the interactive console. Could you think of the reason for those
differences?


## Note on notation

Throughout this course, we will be illustrating examples on the interactive console. We will use the following notation
```text
>>> <command>
<output>
```
where `<command>` stands for the line of code being shown and `<output>` is its output when executed in the interactive console.

This notation can be "stacked":
```text
>>> <command 1>
<output 1>
>>> <command 2>
>>> <command 3>
<output 3>
```
meaning that the lines shown are executed one after the other in the same session.

