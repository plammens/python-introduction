# ----- special float values -----
# besides decimal numbers, the float type has a few special values:
float('+inf')  # positive infinity
float('-inf')  # negative infinity
float('NaN')  # 'not a number'

# NaN isn't equal to anything---not even to itself!
nan = float('nan')
nan == nan  # False


# ----- float limitations -----
# the precision of floating point numbers is limited
0.1 + 0.1 + 0.1
# representation of floating point numbers is hardware-dependent
# most machines use the "double precision" format defined in the IEEE-754 standard, which provides
# 53 bits of precision for the mantissa and 11 bits for the exponent, meaning float values are
# limited to a range between about 0b1.111... * -2**1023 and 0b1.111... * 2**1023
float.fromhex('0x1.fffffffffffffp+1023')  # largest number (in absolute value)
float.fromhex('0x0.0000000000001p-1022')  # smallest number (in absolute value)
