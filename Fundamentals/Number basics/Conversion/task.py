# ----- conversion to int ------
# we can use the int type to convert compatible objects to integers
int('123_000')  # from literal
int('010101', base=2)  # from base 2 literal
int(3.9)  # from float (truncates down to nearest integer)
int(True)  # 1
int(False)  # 0


# ----- conversion to float ------
# we can use the float type to convert compatible objects to floats
float('123.45')  # from literal
float('3.14e0')  # from literal
float.fromhex('0x1.1FA7E2p+22')  # from hex literal
float(42)  # from int
float(True)  # 1.0
float(False)  # 0.0
