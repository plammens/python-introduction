# all of the following are type objects: they're an object representing a type of object
str, int, float, list, set, dict

# thus, their type is... 'type'!
print(type(int))
print(type(str))
print(type(float))

# in fact, even `type` is a type (it's the type of type objects):
print(type(type))
