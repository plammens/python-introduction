# ----- numeric types -----

# -- integers --
int  # type object ("official" name)

123456
0
-123
100_000_000_000_000_023_000_000  # can use underscore as separator
print(-78849101548941)

# -- floats (machine representation of decimal numbers) --
float  # type object ("official" name)

1.20
0.2
.2  # can omit the 0
2.35e5  # exponential notation (2.35e5 is the same as 2.35*10^5)
1.  # have to include the decimal point if you want it to be grades float (and not an integer)

# careful! floats can give surprises due to their limited precision:
0.1 + 0.1 + 0.1  # the value of this is 0.30000000000000004
print(f"0.1 + 0.1 + 0.1 == {0.1 + 0.1 + 0.1}")
