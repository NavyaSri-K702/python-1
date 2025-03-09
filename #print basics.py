#print basics
print("NavyaSri")

#write a program for a single line and multi-line comments
print("single-line comment")
print("multi-line comment")

#different datatypes
a=-7
print("TYpe of a:",type(a))
b=True
print("Type of b:",type(b))
c=5.0
print("Type of c:",type(c))
d='Navya'
print("Type of d:",type(d))

#Define the local and global variables with the same name and print both variables and understand the scope of variables
a=7
def f():
    print("Inside f():",a)
def g():
    a=5
    print("Inside g():",a)
def h():
    global a
    a=2
    print("Inside h():",a)
print("global:",a)
f()
print("global:",a)
g()
print("global:",a)
h()
print("global:",a)
