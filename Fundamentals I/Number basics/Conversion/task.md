# Numbers: conversion

## Conversion between number types

`int`s can be converted to `float`s with the `float` function:
```python
float(12)  # 12.0
```
and viceversa with the `int` function (in which case the fractional part is discarded):
```python
int(12.9)  # 12
```


## String to number

Number objects can also be created, with the `int` or `float` function, from adequate number literals as strings:
```python
int('42')  # 42
int('0b10101', base=2)  # 0b10101
int('10101', base=2)  # 0b10101~~~~
```
```python
float('15e2')  # 15e2
float('-12.5')  # -12.5
float.fromhex('0x1.1FA7E2p+22')  # from hex literal
```

This is useful, for instance when parsing text input from a user as a number.

Leading and trailing spaces don't matter:
```python
int(' 42 ')  # 42
```


## Task

Your goal is to print the result of `(num1 - num2)*3`. The problem is that someone stored the numbers in `num1` and `num2` as strings instead of `int`s or `float`s! 

Use the appropriate conversion functions to convert `num1` and `num2` in the expression inside the print statement.