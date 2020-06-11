# ----- examples of statements (each separated by a blank line): -----
import math  # import statement

my_variable = 42  # assignment statement

del my_variable  # del statement

if __name__ == '__main__':              # if statement
    print('executing as script')        #
else:                                   #
    print('false')                      #

assert True  # assert statement

13 + 45  # expression statement (a statement which only evaluates an expression when executed)

print("hello world")  # expression statement


# ----- examples of expressions (each on its own line): -----
42  # an integer literal
"a string"  # a string literal
None  # the special value None (which is also a keyword)
2*(3 + 1)  # the expression '(3 + 1)' is nested within the expression '2*(3 + 1)'
12*3 + 10**(42//7)
str(123)  # a function call is an expression because it has a value (the return value of the call)
print("hello world") is None  # print is a function, so calling it is an expression with a value

