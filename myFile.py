print("This is my first file")

aList = [1,2,3,"pop","sunday"]

# for item in aList:
#     print(item)
#     if item == "sunday":
#         print("yay")

"""this is a docstring
    which means it's a
    multi-line comment
    """

import sys #helps python program talk to your terminal and pull stuff there

def argument_test():
    print(sys.argv, type(sys.argv))
    print(len(sys.argv))
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2], type(sys.argv[2]))

if __name__ == '__main__':
    """this is really common. it's trying to access
what is the module you're trying to run. it's better than calling the function
directly because the name might change but you could call it from different
contexts and it can do different things"""
    argument_test()

x, y, z = 3, True, "hello" #easier way of declaring 3 variables instead of x=3, y=True...