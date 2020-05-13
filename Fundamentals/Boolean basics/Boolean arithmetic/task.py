# boolean arithmetic

# not - unary operation
not False
not True


# and - binary operation
False and False
False and True
True and False  # order doesn't matter
True and True


# or - binary operation
False and False
False and True
True and False  # order doesn't matter
True and True


# can be combined together arbitrarily:
(True and False) or not (False or (False and True))

# evaluation priority:
# 1. not
# 2. and
# 3. or
