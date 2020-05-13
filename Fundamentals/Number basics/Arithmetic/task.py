import random

# ------ arithmetic operations ------
# All of the familiar arithmetic operations are supported:

12.2 + 13  # addition

18 - 15  # subtraction

2*3.5  # multiplication

7/3  # exact division ("exact" quotient as a floating point number)

11//3  # integer division (division truncated down to nearest integer)

13 ** 2  # exponentiation

7 % 3  # modulus/remainder

# -- mixing ints and floats --
# operating two numbers where at least one of them is a float always returns a float
type(1 + 1.0)
# some operations always return a float even for two integers, e.g. division with /
type(6/2)

# -- modulus (%) --
# (a % b) is the non-negative number c such that a == b*(a//b) + c
# i.e. the difference between the nearest multiple of b that is less than or equal to a, and a
# the modulus operator is useful to check whether a number is multiple of another:
num = random.randint(0, 1000)  # generate a random number between 0 and 1000
k = 3
# if the remainder of dividing num by k is 0 (i.e. num % k == 0), then num is a multiple of k
print(f"is {num} a multiple of {k}? {num % k == 0}")
