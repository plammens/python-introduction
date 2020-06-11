# Comments
**Relevant official docs:** [Comments <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_py.png">](https://docs.python.org/3/reference/lexical_analysis.html#comments)

In the previous lessons, you'll probably have noticed a bunch of text in Python files written
`# like this`. What are these lines starting with a hash? These are comments.

Comments are snippets of text that you add to Python files to explain something that's going on
in the code to human readers.

The Python interpreter doesn't care about comments—these are only useful to someone reading
the source file.

Comments are very useful for others trying to understand your code—this includes yourself after
a few years!

Finding a balance between too few comments and too many is a key skill in a mature programmer!


## How to comment?

To insert one-line comment, use the hash character: everything after `#` up to the end of the line will be considered a comment.

```python
print("Hello, world!")  # this is a one-line comment
```

One-line comments can start anywhere in the line, but they always end at the end of the line
(you cannot "close" them and keep writing code on the same line).

```python
print()  # a comment lasts 'till # the # end # of the line
```


## Task

Look at the file open in the editor; it contains some examples of comments.
Try adding some of your own!
