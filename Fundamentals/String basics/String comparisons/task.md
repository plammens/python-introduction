# Strings: comparisons

## Equality

Strings can be compared for equality as expected.
```python
"abc" == 'abc'
```

A string is equal to another if and only if both are the same length and contain the same characters, in the same order.

## Order

Strings also define an order, so they can also be compared with `<`, `<=`, `>`, and `>=` (meaning "less than", "less than or equal to", "greater than", and "greater than or equal to" respectively).
```python
"aaa" < "abc"
'\x01' > '\x00'
'' <= ''
'' >= ''
```

The order defined by strings is lexicographical; i.e. a string is strictly "less" than another b if its first non-matching character comes first in alphabetical order, or if all characters match, if it is shorter.

In other words, comparing strings is done character by character. We first take a character from the first string and one from the second. If they are equal, we advance both characters. We do that until one of the strings runs out of characters, in which case the latter is the shorter, or until we find a pair of corresponding characters (one from each string, in the same position), in which one is smaller (alphabetically) than the other.

All the following comparisons evaluate to `True`:
```python
"a" < "b"
"A" < "a"
"z" < "za"
"aaz" < "aba"
```

