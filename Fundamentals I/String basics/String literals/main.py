# ----- string literals -----

"hello world"  # a string literal
'hello world'  # using single-quotes---exact same thing
""  # an empty string

# unlike other languages, there's no special type for single characters;
# they're just one-character strings
print(type('a'))  # str

# -- multiline strings --
"""Multiline strings can be split over several lines.
The line breaks in the string literal are reflected in the string object that is created.
This is a new line."""

print("""First line
Second line""")  # prints on two separate lines

'''there's also
the single-quote variety'''  # multiline string using single quotes

