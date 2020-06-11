try:
    from .helper import obj, num
except ImportError:
    from helper import obj, num


# your solution goes here
boolean1 = isinstance(obj, list) or isinstance(obj, str) and obj[0] == 'x'
boolean2 = isinstance(num, float) and 0 <= num <= 1 or isinstance(num, int) and 0 <= num <= 100
boolean3 = not isinstance(obj, list)
boolean4 = num < float('+inf')

# extra thinking exercise (optional)
print(boolean1)
print(boolean2)
print(boolean3)
print(boolean4)
