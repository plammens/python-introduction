# ----- sequence types -----

# -- lists (ordered sequences of objects) --
list  # type object ("official" name)

[1, 'abc', 2.3, 2.3]  # syntax for a list: comma-separated list in square brackets
sample_list = [1, 'abc', 2.3, 2.3]  # a list can contain objects of any kind!
sample_list[1]  # get the element at position 1
sample_list[0] = 'spam'  # set the element at position 0 to 'spam'
print(sample_list[0])  # python is 0-indexed: starts counting from 0!

# -- tuples (same as lists, but they have a fixed size and can't be modified) --
tuple  # type object ("official" name)

(1, 'abc', 2.3, 2.3)  # syntax for a tuple: comma-separated list in parentheses
sample_tuple = (1, 'abc', 2.3, 2.3)  # a list can contain objects of any kind!
sample_tuple[1]  # get the element at position 1
