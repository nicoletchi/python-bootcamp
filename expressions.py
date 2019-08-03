x = 15 
y = 3
#python assumes x is whatever you put into it - int in this case

z = "this is a string"
a = "hello"
b = "world"
c = "again"

#print("x / y =", x/y)
#print(a + b + c)
#print(a,b,c)

#for i in range(0,50,5):
#    print(i)
#increments by 5 from 0 to 50

myList = [1,2,3,4,5]
#for i in myList:
#    print(i)

def myPrint(words):
    print(words, ", ok.")

def myFunction(start, vlist, step):
    for i in range(start, len(vlist),step):
        print(vlist[i])

#myFunction(["hello", 1, True, 3.14159])
#sticks in each of these values into myFunction one at a time

myFunction(1, ["hello", 1, True, 3.14159], 2)

def myRecursiveFunction(vlist):
    if len(vlist) > 0:
        print(vlist.pop())
        myRecursiveFunction(vlist)
#to get comfortable with recursion, write things in for loops and then see if you can write it in recursion as well

myRecursiveFunction(["hello", 1, True, 3.14159])


