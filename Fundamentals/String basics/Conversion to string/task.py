# ----- conversion to string -----
# every object has a string representation---that's what gets printed when we use print on something
# which isn't a string
print(object())

# you can explicitly convert objects to strings using the str type:
print(str(object()))  # equivalent to above
str(2.3e4)
type(str(42)) is str
