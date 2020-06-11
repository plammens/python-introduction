
# lists are sequences of objects
my_list = ["abc", 42, 3.14, object()]

# length
len(my_list)

# indexing
my_list[0]
my_list[1]

# changing elements
my_list[2] = -1

# negative indices
my_list[-1]
my_list[-2]

# out of range
my_list[4]


# slice
my_list[1:3]
my_list[:]
my_list[1:]
my_list[:3]


# append(element)
my_list.append("another element")


# insert(index, element)
my_list.insert(0, "element 0")
my_list.insert(2, "element 2")


# del
del my_list[2]
del my_list[0]

# extend (in-place modification)
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)


# clear
my_list.clear()


# + operator (new list)
a = [1, 2, 3]
b = [4, 5, 6]

a + b


# * operator (new list)
[1, 2, 3] * 5
my_list = [object()] * 5

