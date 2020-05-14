# ----- strings as a sequence of characters -----

# strings have a length, which corresponds to the number of characters they contain:
len("abcdef")  # we use the `len` function to get the length of a string
print(len(""))  # prints 0
print(len("abc\ndef"))  # prints 7 ('\n' counts as a single character)

# we can get the i-th character of a string (counting from 0) using subscript notation:
"hello"[0]  # gets the first character, i.e. 'h'
# this returns a string of length 1 with the corresponding character:
print('hello'[0])
print(type("hello"[0]))  # str
print(len('hello'[0]))  # 1
