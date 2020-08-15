# common for loop recipes


# Repetition
# for when you just want to repeat something a number of times
for _ in range(5):
    # convention: _ is used to indicate that you don't care about the value
    print("Doing something")


# Range iteration
# doing something for every integer in a range
for x in range(1, 10, 2):  # odd numbers from 1 to 10
    print(x**2)  # do something with x


# Range iteration for indexing
# same as previous, but specifically for indexing a sequence, e.g. a list or a str
my_list = [3, "word", 2, -1, "foo"]
for i in range(len(my_list)):
    print(my_list[i], my_list[-i - 1])


# Iterating over a collection
# doing something exactly once for each element in the collection, in order
collection = {"hi", 3, 3, 1, 5,}
for element in collection:
    print(element)

collection = [1, 1, 3, 5, 7]
for element in collection:
    print(element**2)


# Iterating over a dictionary
d = {"Bob": 63, "Alice": 89, "Charlie": 77}

# dictionary keys
for key in d:
    print(key)

# dictionary values
for value in d.values():
    print(value)

# (key, value) pairs
for key, value in d.items():
    print(key, value)


# Constructing a list
# add an element to the end of the list at each iteration
my_list = []
for x in range(0, 10, 3):
    elem = x//2  # compute an element to add to the list...
    my_list.append(elem)  # add it to the list


# Iterating over a collection keeping track of the index
# we get the element and its index in two loop variables
for i, elem in [3, "word", 2, -1, "foo"]:
    print(i, elem)


# Searching for a specific element
# this uses the break keyword to stop iterating as soon as it is found
target = -1
for elem in [3, "word", 2, -1, "foo"]:
    if elem == target:
        print("found")
        break  # exit the loop early
else:  # if the loop terminates normally without having "break"ed out of it
    print("not found")


# Skip an element
# like iterating over a collection, but skipping an element
skip = 2
for elem in [3, "word", 2, -1, "foo"]:
    if elem == skip:
        continue  # jump to the next iteration
    print(elem)


# Iterate two (or more) collections in parallel
# usage of `zip`
collection1 = ["foo", "bar", "baz"]
collection2 = [42, -2, 100]
for x, y in zip(collection1, collection2):
    print(x, y)
