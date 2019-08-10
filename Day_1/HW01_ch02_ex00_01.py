# HW01_ch02_ex00_01
# See section 2.4
# (1) Type the following statements in the Python interpreter to see what they
# do:
# 5
# x = 5
# x + 1
#
# (2) Now put the same statements into a script [this script] and run it.
# enter statements below this line ########

print(5)
print("x = 5")
print("x + 1")

print("Hello World!")  # example


# enter statements above this line ########
# What is the output?
# Hello World!
#
# (3) Modify the script above by transforming each expression into a print
# statement and then run it again.
# What is the output?

#If I don't put the 2nd and 3rd expression in quotes, I get the following traceback:
# 5
#Traceback (most recent call last):
#  File "HW01_ch02_ex00_01.py", line 13, in <module>
#    print(x=5)
#TypeError: 'x' is an invalid keyword argument for print()

#If I do put the expressions in quotes, the output is:
#5
#x = 5
#x + 1
#Hello World!
