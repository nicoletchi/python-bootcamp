#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and
# goes to the next line.


# (2) Write a function that draws a similar grid with four rows and four
# columns.
###############################################################################
# Write your functions below:

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    
def bar():
    print('- - - - +', end = ' ')

def column():
    print('         /', end='')

def horizontal(f, v):
    print('+', end = ' ')
    f(v)
    print()

    
def vertical(f, v):
    print('/', end = '')
    f(v)
    print()

def verticalStacked(f):
    vertical(f, column)
    vertical(f, column)
    vertical(f, column)
    vertical(f, column)

def two_by_two():
    horizontal(do_twice, bar)
    verticalStacked(do_twice)
    horizontal(do_twice, bar)
    verticalStacked(do_twice)
    horizontal(do_twice, bar)

def one_by_four():
    horizontal(do_four, bar)
    verticalStacked(do_four)
    
def four_by_four():
    do_four(one_by_four)
    horizontal(do_four, bar)

# Write your functions above:
###############################################################################
def main():
    
    two_by_two()
    four_by_four()


if __name__ == "__main__":
    main()
