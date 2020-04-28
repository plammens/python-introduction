# examples of objects:
123
"hello world"
object()
["this", "is", "a", "list"]
12.5

# ----- comparing the value of objects -----
a = "hello"
b = 'hello'

print(a == b)  # prints True
print(a != b)  # prints False

# ------ comparing the identity of objects -----
a = [1, 2, 3]
b = [1, 2, 3]

# two objects can be equal but have different identities!
print(a == b)  # prints 'True'
print(a is b)  # prints 'False'

# but identical objects are always equal (with very few exceptions):
b = a
print(a is b)  # prints 'True'
print(a == b)  # prints 'True'

# conclusion: identical objects are always equal in value (for obvious reasons)
# but equal objects need not be identical (i.e. they can be separate objects).


# ------ the type of objects -----

print(type(a))  # prints 'list'
print(type(123))
print(type("foobar"))
