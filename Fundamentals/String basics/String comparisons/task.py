# ----- Comparisons between strings -----
# strings can be compared for equality as expected:
"abc" == 'abc'
print("an" + " " + "apple" == "an apple")  # True
print("hello" == 'hello')  # True
print("spam\neggs" != '''spam
eggs''')  # False

# strings also define an order, so can be compared with <, <=, >, >=:
"aaa" < "abc"
'\x01' > '\x00'
'' <= ''
'' >= ''
print("a" <= "a")  # prints True

# the order is lexicographical; a string is strictly "less" than another b if its first
# non-matching character comes first in alphabetical order, or if it is shorter if all characters
# match. All of the following are True:
"a" < "b"
"A" < "a"
"z" < "za"
"aaz" < "aba"
